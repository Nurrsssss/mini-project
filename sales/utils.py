from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_invoice_pdf(order):
    template_path = "sales/invoice_template.html"
    context = {"order": order}
    template = get_template(template_path)
    html = template.render(context)

    response = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), response)
    
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type="application/pdf")
    return None
