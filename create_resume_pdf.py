from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch

def create_pdf():
    doc = SimpleDocTemplate(
        "static/Dhanesh_Cybersecurity_Resume.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    # Read the content from the text file
    with open('static/resume.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    # Create styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['BodyText'],
        spaceBefore=6,
        spaceAfter=6,
        fontSize=10,
        leading=14,
    ))
    
    styles.add(ParagraphStyle(
        name='Header',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=20,
        textColor=colors.HexColor('#006400'),  # Dark green for cybersecurity theme
    ))

    # Convert content to paragraphs
    story = []
    for line in content.split('\n'):
        if line.strip():
            if any(section in line for section in ['OBJECTIVE', 'EDUCATION', 'SKILLS', 'PROJECTS', 'CERTIFICATIONS', 'WORKSHOPS', 'CAREER', 'LANGUAGES']):
                story.append(Paragraph(line, styles['Header']))
            else:
                story.append(Paragraph(line, styles['CustomBody']))
        else:
            story.append(Spacer(1, 12))

    # Build the PDF
    doc.build(story)

if __name__ == '__main__':
    create_pdf() 