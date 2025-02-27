from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_report_pdf(report_data):
    template_path = "analytics/report_template.html"
    context = {"report_data": report_data}
    template = get_template(template_path)
    html = template.render(context)

    response = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), response)
    
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type="application/pdf")
    return None
