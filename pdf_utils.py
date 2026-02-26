from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import markdown2
import re
from io import BytesIO


def clean_markdown(md_text: str) -> str:
    """
    Convert markdown to clean readable plain text
    """
    html = markdown2.markdown(md_text)

    # Remove HTML tags
    clean_text = re.sub('<[^<]+?>', '', html)

    # Fix extra newlines
    clean_text = clean_text.replace('\n\n', '\n')

    return clean_text


def create_pdf(text):

    buffer = BytesIO()

    cleaned_text = clean_markdown(text)

    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    x_margin = 1 * inch
    y_position = height - 1 * inch

    c.setFont("Helvetica", 10)

    for line in cleaned_text.split("\n"):

        if y_position < 1 * inch:
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = height - 1 * inch

        c.drawString(x_margin, y_position, line)
        y_position -= 14

    c.save()

    buffer.seek(0)
    return buffer.getvalue()