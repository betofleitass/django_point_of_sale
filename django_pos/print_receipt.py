from django_pos.wsgi import *
from django_pos import settings
from django.template.loader import get_template
from weasyprint import HTML, CSS


def print_receipt():
    template = get_template("sales/receipt_pdf.html")
    context = {"name": "Jorge"}
    html_template = template.render(context)

    # CSS Boostrap
    css_url = os.path.join(
        settings.BASE_DIR, 'static/css/receipt_pdf/bootstrap.min.css')

    # Create the pdf
    HTML(string=html_template).write_pdf(
        target="receipt.pdf", stylesheets=[CSS(css_url)])


print_receipt()
