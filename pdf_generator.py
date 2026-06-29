from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib import colors


class PDFGenerator:
    def __init__(self, filename="CV.pdf"):
        self.filename = filename
        self.doc = SimpleDocTemplate(
            filename, pagesize=A4,
            rightMargin=0.7 * inch, leftMargin=0.7 * inch,
            topMargin=0.5 * inch, bottomMargin=0.5 * inch
        )
        self.styles = self._create_styles()
        self.elements = []

    def _create_styles(self):
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='CVName', parent=styles['Heading1'],
                                  fontSize=24, textColor=colors.HexColor('#2C3E50'),
                                  spaceAfter=4, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='CVTitle', parent=styles['Normal'],
                                  fontSize=12, textColor=colors.HexColor('#7F8C8D'),
                                  spaceAfter=8, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='ContactInfo', parent=styles['Normal'],
                                  fontSize=9, alignment=TA_CENTER,
                                  textColor=colors.HexColor('#34495E')))
        styles.add(ParagraphStyle(name='SectionTitle', parent=styles['Heading2'],
                                  fontSize=13, textColor=colors.HexColor('#2C3E50'),
                                  spaceBefore=10, spaceAfter=6,
                                  fontName='Helvetica-Bold'))
        styles.add(ParagraphStyle(name='NormalText', parent=styles['Normal'],
                                  fontSize=10, leading=13))
        styles.add(ParagraphStyle(name='JobTitle', parent=styles['Normal'],
                                  fontSize=11, textColor=colors.HexColor('#2C3E50'),
                                  fontName='Helvetica-Bold'))
        return styles

    def add_header(self, info):
        self.elements.append(Paragraph(info["name"], self.styles['CVName']))
        self.elements.append(Paragraph(info["title"], self.styles['CVTitle']))
        contact = f"{info['email']}  |  {info['phone']}  |  {info['address']}"
        self.elements.append(Paragraph(contact, self.styles['ContactInfo']))
        if info.get('linkedin') or info.get('github'):
            links = "  |  ".join(filter(None, [info.get('linkedin'), info.get('github')]))
            self.elements.append(Paragraph(links, self.styles['ContactInfo']))
        self.elements.append(HRFlowable(width="100%", thickness=1,
                                        color=colors.HexColor('#BDC3C7')))

    def add_section_title(self, title):
        self.elements.append(Spacer(1, 0.1 * inch))
        self.elements.append(Paragraph(title.upper(), self.styles['SectionTitle']))
        self.elements.append(HRFlowable(width="100%", thickness=0.5,
                                        color=colors.HexColor('#BDC3C7')))

    def add_summary(self, text):
        self.elements.append(Paragraph(text, self.styles['NormalText']))

    def add_experience(self, experiences):
        for exp in experiences:
            line = f"<b>{exp['position']}</b> — {exp['company']}"
            self.elements.append(Paragraph(line, self.styles['JobTitle']))
            self.elements.append(Paragraph(f"<i>{exp['period']}</i>",
                                           self.styles['NormalText']))
            for resp in exp['responsibilities']:
                self.elements.append(Paragraph(f"• {resp}", self.styles['NormalText']))
            self.elements.append(Spacer(1, 0.05 * inch))

    def add_education(self, education):
        for edu in education:
            line = f"<b>{edu['degree']}</b> — {edu['school']}"
            self.elements.append(Paragraph(line, self.styles['JobTitle']))
            details = edu['year']
            if edu.get('gpa'):
                details += f"  |  GPA: {edu['gpa']}"
            self.elements.append(Paragraph(details, self.styles['NormalText']))
            self.elements.append(Spacer(1, 0.05 * inch))

    def add_skills(self, skills):
        skills_text = "  •  ".join(skills)
        self.elements.append(Paragraph(skills_text, self.styles['NormalText']))

    def add_projects(self, projects):
        for proj in projects:
            self.elements.append(Paragraph(
                f"<b>{proj['name']}</b> <i>({proj['tech']})</i>",
                self.styles['JobTitle']))
            self.elements.append(Paragraph(proj['description'],
                                           self.styles['NormalText']))
            self.elements.append(Spacer(1, 0.05 * inch))

    def save(self):
        self.doc.build(self.elements)
