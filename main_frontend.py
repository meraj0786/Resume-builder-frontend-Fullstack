from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Register a nice font (optional)
# pdfmetrics.registerFont(TTFont('Helvetica-Bold', 'Helvetica-Bold.ttf'))

def create_beautiful_resume():
    doc = SimpleDocTemplate(
        "Meraj_Ali_Resume_React.pdf",
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    # Styles
    styles = getSampleStyleSheet()
    # styles.add(ParagraphStyle(name='TitleCenter', fontSize=24, leading=28, alignment=TA_CENTER, spaceAfter=10, fontName='Helvetica-Bold'))
    # styles.add(ParagraphStyle(name='TitleCenter2', fontSize=16, leading=28, alignment=TA_CENTER, spaceAfter=10, textColor=colors.HexColor('#1A237E'), fontName='Helvetica-Bold'))
    # styles.add(ParagraphStyle(name='Heading1Left', fontSize=16, leading=20, spaceAfter=6, textColor=colors.HexColor('#1A237E'), fontName='Helvetica-Bold'))
    # styles.add(ParagraphStyle(name='Heading2Left', fontSize=14, leading=18, spaceAfter=4, textColor=colors.black, fontName='Helvetica-Bold'))
    # styles.add(ParagraphStyle(name='NormalLeft', fontSize=11, leading=14, spaceAfter=2))
    # styles.add(ParagraphStyle(name='ContactInfo', fontSize=10, leading=12, alignment=TA_CENTER, spaceAfter=12))

    styles.add(ParagraphStyle(name='TitleCenter', fontSize=20, leading=22, alignment=TA_CENTER, spaceAfter=4, fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle(name='TitleCenter2', fontSize=14, leading=16, alignment=TA_CENTER, spaceAfter=4, textColor=colors.HexColor('#00BFFF'), fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle(name='Heading1Left', fontSize=12, leading=14, spaceAfter=2, textColor=colors.HexColor('#00BFFF'), fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle(name='Heading2Left', fontSize=11, leading=13, spaceAfter=1, textColor=colors.black, fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle(name='NormalLeft', fontSize=9, leading=11, spaceAfter=1))
    styles.add(ParagraphStyle(name='ContactInfo', fontSize=8, leading=10, alignment=TA_CENTER, spaceAfter=6))

    story = []

    # Name and Title
    story.append(Paragraph("Meraj Ali", styles['TitleCenter']))
    story.append(Paragraph("Software Development Engineer", styles['TitleCenter2']))
    contact_text = """
    +91 9990302054 | meraj4382@gmail.com | Delhi, India<br/>
    <a href='https://www.linkedin.com/in/meraj-ali-34770917a' color='blue'>LinkedIn</a> | 
    <a href='https://github.com/meraj0786' color='blue'>GitHub</a>
    """
    story.append(Paragraph(contact_text, styles['ContactInfo']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.grey))
    story.append(Spacer(1, 12))

    # Professional Summary
    story.append(Paragraph("Professional Summary", styles['Heading1Left']))
    summary_text = (
    "Frontend Developer with 3.10 years of experience building responsive, scalable, and high-performance web applications. "
    "Proficient in React.js, Next.js, JavaScript (ES6+), HTML5, CSS3, Bootstrap, Material-UI, and Tailwind CSS. "
    "Skilled in RESTful API integration, cross-browser compatibility, and performance optimization. "
    "Strong team player experienced in Agile environments, focused on delivering user-friendly and accessible UI solutions."
    )

    story.append(Paragraph(summary_text, styles['NormalLeft']))
    story.append(Spacer(1, 12))

    # Skills
    story.append(Paragraph("Skills", styles['Heading1Left']))
    skills_text = (
        "JavaScript (ES6+), React.js, Next.js, Node.js, jQuery, HTML5, CSS3, Bootstrap, Material-UI, Tailwind CSS, Redux, Context API, RESTful APIs, JSON, Axios, Fetch, "
        "npm/yarn, UI/UX Best Practices, Python, FastAPI, REST API,  SQL (MySQL),  Git, Object-Oriented Programming.  "
    )
    story.append(Paragraph(skills_text, styles['NormalLeft']))
    story.append(Spacer(1, 12))

    # Work Experience
    story.append(Paragraph("Work Experience", styles['Heading1Left']))
    story.append(Paragraph("Software Developer", styles['Heading2Left']))
    story.append(Paragraph("Agriculture Insurance Company of India Limited (Talent Pro), New Delhi, India", styles['NormalLeft']))
    story.append(Paragraph("2023 – Present", styles['NormalLeft']))
    work_bullets = [
    "Developed and maintained the official AIC website using React.js with responsive, mobile-friendly design.",
    "Built reusable components and integrated RESTful APIs for dynamic modules.",
    "Optimized performance with code splitting, lazy loading, and Redux/Context state management.",
    "Ensured accessibility (WCAG) and implemented SEO-friendly practices."
    ]

    story.append(ListFlowable([ListItem(Paragraph(b, styles['NormalLeft'])) for b in work_bullets], bulletType='bullet'))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("Associate Software Engineer", styles['Heading2Left']))
    story.append(Paragraph("Tech Mahindra, Noida, NSEZ", styles['NormalLeft']))
    story.append(Paragraph("11/2021 – 02/2023", styles['NormalLeft']))
    work_bullets = [
        'Built and optimized React.js components with Redux/Context API for product listings, cart, and checkout flows.',
        'Implemented reusable UI modules with React hooks, improving feature delivery and maintainability.',
        'Developed custom form validations for address, payment, and registration forms to ensure accurate data capture.',
        'Integrated OAuth-based social logins (Google, Facebook) with backend APIs for seamless user onboarding.',
        'Enhanced page load performance with code splitting, lazy loading, and API response handling.'
    ]
    story.append(ListFlowable([ListItem(Paragraph(b, styles['NormalLeft'])) for b in work_bullets], bulletType='bullet'))
    story.append(Spacer(1, 12))

    # Projects
    story.append(Paragraph("Projects", styles['Heading1Left']))
    projects = {
        'AIC Official Website Revamp (React.js) | 2023 - 2024': [
            "Led frontend revamp of aicofindia.com using React.js, Bootstrap, and Material-UI, improving UX and interface design.",
            "Developed dynamic modules for policy details, claims, and customer dashboards.",
            "Managed complex UI states with Redux/Context and optimized performance for faster load times.",
            "Delivered scalable, maintainable code following best practices and Git version control."
        ],

       'PMFBY (Pradhan Mantri Fasal Bima Yojana) | 2024 – Present': [
            "Developed React.js frontend integrated with Flask APIs for nationwide crop insurance operations.",
            "Built reporting, claim workflows, and survey modules to streamline farmer–insurer interactions.",
            "Implemented interactive data visualizations and historical/state-wise claim insights.",
            "Enabled Excel report generation, bulk upload, and inline data edits for large datasets."
        ],

        'AMS (Asset Management System) | 2024 - Present': [
            "Developed React.js frontend integrated with Flask APIs for managing company-wide assets.",
            'Built modules for asset allocation, tracking, and lifecycle management with role-based access.',
            'Implemented Excel upload/export and bulk operations for faster asset management workflows.'
            'Added interactive dashboards and reports with filtering/search for quick decision-making.'
        ]
        
    }
    
    for project, bullets in projects.items():
        story.append(Paragraph(project, styles['Heading2Left']))
        story.append(ListFlowable([ListItem(Paragraph(b, styles['NormalLeft'])) for b in bullets], bulletType='bullet'))
        story.append(Spacer(1, 6))
        
    # second work experience
    # story.append(Paragraph("Work Experience", styles['Heading1Left']))
    # story.append(Paragraph("Associate Software Engineer", styles['Heading2Left']))
    # story.append(Paragraph("Tech Mahindra, Noida, NSEZ", styles['NormalLeft']))
    # story.append(Paragraph("11/2021 – 02/2023", styles['NormalLeft']))
    # work_bullets = [
    #     'Built and optimized React.js components with Redux/Context API for product listings, cart, and checkout flows.',
    #     'Implemented reusable UI modules with React hooks, improving feature delivery and maintainability.',
    #     'Developed custom form validations for address, payment, and registration forms to ensure accurate data capture.',
    #     'Integrated OAuth-based social logins (Google, Facebook) with backend APIs for seamless user onboarding.',
    #     'Enhanced page load performance with code splitting, lazy loading, and API response handling.'
    # ]
    # story.append(ListFlowable([ListItem(Paragraph(b, styles['NormalLeft'])) for b in work_bullets], bulletType='bullet'))
    # story.append(Spacer(1, 12))

    # Education
    story.append(Paragraph("Education", styles['Heading1Left']))
    education_list = [
        ('BACHELOR IN TECHNOLOGY (B.TECH)', 'J.C. Bose University of Science and Technology, YMCA', '2017 – 2021', 'GPA: 7.43/10.0')
    ]
    for degree, institute, years, gpa in education_list:
        story.append(Paragraph(f"<b>{degree}</b><br/>{institute} | {years} | {gpa}", styles['NormalLeft']))
        story.append(Spacer(1, 6))

    # Languages
    # story.append(Paragraph("Languages", styles['Heading1Left']))
    # story.append(Paragraph("English, Hindi, Urdu", styles['NormalLeft']))
    # story.append(Spacer(1, 12))

    # Strengths
    story.append(Paragraph("Strengths", styles['Heading1Left']))
    strengths = [
        'Strong problem-solving and analytical skills, Commitment to continuous learning and technology advancement.',
        'Effective time management and prioritization, Knowledge of software testing and quality assurance.',
    ]
    story.append(ListFlowable([ListItem(Paragraph(s, styles['NormalLeft'])) for s in strengths], bulletType='bullet'))

    # Build PDF
    doc.build(story)

if __name__ == "__main__":
    create_beautiful_resume()
