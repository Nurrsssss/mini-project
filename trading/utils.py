from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from trading.models import Transaction, Order


def send_order_update(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "orders",
        {"type": "order_message", "message": message}
    )

def match_orders(new_order):
    opposite_type = 'sell' if new_order.order_type == 'buy' else 'buy'
    matching_orders = Order.objects.filter(
        product=new_order.product,
        order_type=opposite_type,
        price_per_unit=new_order.price_per_unit
    ).order_by('created_at')

    for match in matching_orders:
        trade_quantity = min(new_order.quantity, match.quantity)
        total_price = trade_quantity * new_order.price_per_unit

        transaction = Transaction.objects.create(
            buyer=new_order.user if new_order.order_type == 'buy' else match.user,
            seller=match.user if new_order.order_type == 'buy' else new_order.user,
            product=new_order.product,
            quantity=trade_quantity,
            total_price=total_price,
        )

        send_order_update(f"Новая сделка! {trade_quantity}x {transaction.product.name} по цене {transaction.total_price}")

        new_order.quantity -= trade_quantity
        match.quantity -= trade_quantity

        if match.quantity == 0:
            match.delete()
        else:
            match.save()

        if new_order.quantity == 0:
            new_order.delete()
            break

    if new_order.quantity > 0:
        new_order.save()