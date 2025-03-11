from django.utils.timezone import now, timedelta
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import AnalyticsReport
from sales.models import SalesOrder
from trading.models import Transaction
from users.permissions import IsAdmin

class GenerateSalesReportView(generics.CreateAPIView):
    """
    Генерирует отчёт по продажам за последний месяц.
    Доступно только администратору.
    """
    permission_classes = [IsAdmin]

    def create(self, request, *args, **kwargs):
        last_month = now() - timedelta(days=30)
        sales_orders = SalesOrder.objects.filter(created_at__gte=last_month)

        total_sales = sum(order.total_price for order in sales_orders)
        total_orders = sales_orders.count()

        report = AnalyticsReport.objects.create(
            report_type='sales',
            generated_by=request.user,
            data={
                "total_sales": total_sales,
                "total_orders": total_orders,
                "orders": list(sales_orders.values("id", "total_price", "created_at")),
            }
        )
        return Response({"message": "Sales report generated", "data": report.data})

class GenerateTradingReportView(generics.CreateAPIView):
    """
    Генерирует отчёт по торговым сделкам за последний месяц.
    """
    permission_classes = [IsAdmin]

    def create(self, request, *args, **kwargs):
        last_month = now() - timedelta(days=30)
        transactions = Transaction.objects.filter(created_at__gte=last_month)

        total_traded_volume = sum(t.total_price for t in transactions)
        total_transactions = transactions.count()

        report = AnalyticsReport.objects.create(
            report_type='trading',
            generated_by=request.user,
            data={
                "total_traded_volume": total_traded_volume,
                "total_transactions": total_transactions,
                "transactions": list(transactions.values("id", "total_price", "created_at")),
            }
        )
        return Response({"message": "Trading report generated", "data": report.data})

class GenerateProfitLossReportView(generics.CreateAPIView):
    """
    Генерирует отчёт о прибыли и убытках.
    """
    permission_classes = [IsAdmin]

    def create(self, request, *args, **kwargs):
        last_month = now() - timedelta(days=30)
        sales_revenue = sum(order.total_price for order in SalesOrder.objects.filter(created_at__gte=last_month))
        trading_profit = sum(transaction.total_price for transaction in Transaction.objects.filter(created_at__gte=last_month))

        profit_loss = sales_revenue + trading_profit

        report = AnalyticsReport.objects.create(
            report_type='profit_loss',
            generated_by=request.user,
            data={
                "sales_revenue": sales_revenue,
                "trading_profit": trading_profit,
                "total_profit_loss": profit_loss,
            }
        )
        return Response({"message": "Profit/Loss report generated", "data": report.data})