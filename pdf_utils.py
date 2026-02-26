from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from io import BytesIO

def generate_pdf(itinerary_text):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

    styles = getSampleStyleSheet()

    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontName='STSong-Light',
        fontSize=11,
        leading=15,
    )

    itinerary_text = itinerary_text.replace("₹", "Rs. ")

    elements = []
    for line in itinerary_text.split("\n"):
        elements.append(Paragraph(line, normal_style))
        elements.append(Spacer(1, 0.15 * inch))

    doc.build(elements)

    buffer.seek(0)
    return buffer
