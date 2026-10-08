import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

def build_pdf(filename="resume.pdf"):
    # Target 2 exact pages with Letter size
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()
    
    # Custom Palette
    NAVY = colors.HexColor("#0B1727")
    CYAN = colors.HexColor("#0284C7")
    LIGHT_CYAN = colors.HexColor("#0EA5E9")
    DARK_BLUE = colors.HexColor("#1E3A8A")
    TEXT_DARK = colors.HexColor("#0F172A")
    TEXT_MUTED = colors.HexColor("#475569")
    BG_BOX = colors.HexColor("#F1F5F9")
    BORDER_BOX = colors.HexColor("#CBD5E1")
    WHITE = colors.HexColor("#FFFFFF")

    # Custom Styles
    style_normal = ParagraphStyle('NormalText', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=TEXT_DARK)
    style_muted = ParagraphStyle('MutedText', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=TEXT_MUTED)
    style_bullet = ParagraphStyle('BulletText', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=TEXT_DARK, leftIndent=10)
    
    style_header_name = ParagraphStyle('HeaderName', fontName='Helvetica-Bold', fontSize=22, leading=24, textColor=WHITE)
    style_header_sub = ParagraphStyle('HeaderSub', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=LIGHT_CYAN)
    style_header_contact_title = ParagraphStyle('HeaderContactTitle', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=LIGHT_CYAN, alignment=2)
    style_header_contact = ParagraphStyle('HeaderContact', fontName='Helvetica', fontSize=7.5, leading=10, textColor=WHITE, alignment=2)
    
    style_link_bar = ParagraphStyle('LinkBar', fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=CYAN, alignment=1)
    
    style_sec_title = ParagraphStyle('SecTitle', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=CYAN)
    style_proj_title = ParagraphStyle('ProjTitle', fontName='Helvetica-Bold', fontSize=13, leading=15, textColor=NAVY)
    style_proj_sub = ParagraphStyle('ProjSub', fontName='Helvetica-Bold', fontSize=8, leading=11, textColor=CYAN)
    
    style_stack_head = ParagraphStyle('StackHead', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=CYAN)
    style_stack_label = ParagraphStyle('StackLabel', fontName='Helvetica-Bold', fontSize=7, leading=9, textColor=DARK_BLUE)
    style_stack_val = ParagraphStyle('StackVal', fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=TEXT_DARK)

    story = []

    # ═════════════════════════════════════════════
    # PAGE 1
    # ═════════════════════════════════════════════

    # Top Header Box
    header_left = [
        Paragraph("KUSHANT", style_header_name),
        Spacer(1, 4),
        Paragraph("SOFTWARE / FULL-STACK DEVELOPER", style_header_sub)
    ]
    header_right = [
        Paragraph("CONTACT", style_header_contact_title),
        Paragraph("9289256544", style_header_contact),
        Paragraph("honestlygolu@gmail.com", style_header_contact),
        Paragraph("Delhi, India", style_header_contact)
    ]
    header_table = Table([[header_left, header_right]], colWidths=[330, 210])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4))

    # Links Under Header
    links_p = Paragraph(
        '<font color="#0284C7"><b>linkedin.com/in/developerkushant</b></font> &nbsp;•&nbsp; '
        '<font color="#0284C7"><b>github.com/honestlygolu</b></font>',
        style_link_bar
    )
    story.append(links_p)
    story.append(Spacer(1, 8))

    # Profile Section
    prof_title = Paragraph("<b>PROFILE</b>", style_sec_title)
    prof_body = Paragraph(
        "BCA student focused on software development with hands-on experience building and shipping full-stack web applications. "
        "Strong practical foundation across React, FastAPI, PostgreSQL, Python, SQL, Tailwind CSS, Git and Docker, with a flagship project "
        "that covers real commerce, authentication and payment workflows.",
        style_normal
    )
    prof_table = Table([[prof_title], [prof_body]], colWidths=[540])
    prof_table.setStyle(TableStyle([
        ('LINELEFT', (0,0), (0,-1), 2.5, CYAN),
        ('PADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('BOTTOMPADDING', (0,1), (-1,1), 6),
    ]))
    story.append(prof_table)
    story.append(Spacer(1, 10))

    # Main 2-Column Content for Page 1
    # Left Column: Featured Project & How I Built It
    left_flow = []
    
    left_flow.append(Paragraph("01 FEATURED PROJECT", style_sec_title))
    left_flow.append(Spacer(1, 2))
    left_flow.append(Paragraph("NOVA <font color='#64748B'>|</font> Full-Stack E-Commerce Platform", style_proj_title))
    left_flow.append(Spacer(1, 2))
    left_flow.append(Paragraph("React 19 • Vite • FastAPI • PostgreSQL • SQLAlchemy • Tailwind CSS 4 • Docker • Razorpay", style_proj_sub))
    left_flow.append(Spacer(1, 5))

    bullets_p1 = [
        "• Built a complete multi-page commerce experience with product browsing, product details, saved items, cart, checkout, order confirmation, order history and account flows.",
        "• Implemented guest and authenticated carts with backend persistence, relational order data and product-variant support.",
        "• Developed registration, login, password recovery and reset flows, with database-backed rate limiting across sensitive endpoints.",
        "• Designed API and database layers using FastAPI, SQLAlchemy, PostgreSQL and Alembic migrations for maintainable relational data models.",
        "• Integrated Razorpay test-mode checkout with backend-controlled order creation, payment-event tracking, webhook handling and stock validation.",
        "• Configured Docker Compose with PostgreSQL and Mailpit to make local development and password-recovery testing reproducible."
    ]
    for b in bullets_p1:
        left_flow.append(Paragraph(b, style_bullet))
        left_flow.append(Spacer(1, 3))
    
    left_flow.append(Spacer(1, 2))
    left_flow.append(Paragraph("<b>Repository:</b> <font color='#0284C7'>github.com/honestlygolu/Nova-Ecommerce</font>", style_normal))
    left_flow.append(Spacer(1, 8))

    # How I Built It
    left_flow.append(Paragraph("02 HOW I BUILT IT", style_sec_title))
    left_flow.append(Spacer(1, 4))
    bullets_how = [
        "• <b>Frontend architecture:</b> reusable React components, client-side routing, state-driven cart and account experiences, API integration through Axios.",
        "• <b>Backend architecture:</b> REST-style FastAPI endpoints, Pydantic validation, JWT-based authentication and SQLAlchemy ORM models.",
        "• <b>Data integrity:</b> explicit order and payment records, item/address snapshots for open orders, stock checks and migration-driven schema changes.",
        "• <b>Developer workflow:</b> Git-based feature development, GitHub source control and Dockerized local services for consistent setup."
    ]
    for b in bullets_how:
        left_flow.append(Paragraph(b, style_bullet))
        left_flow.append(Spacer(1, 3))

    # Right Column: Core Stack, Online, Education
    right_flow = []
    right_flow.append(Paragraph("CORE STACK", style_stack_head))
    right_flow.append(Spacer(1, 4))

    stacks = [
        ("LANGUAGES", "Python<br/>JavaScript<br/>SQL<br/>HTML / CSS"),
        ("FRONTEND", "React<br/>Vite<br/>Tailwind CSS<br/>React Router<br/>Axios"),
        ("BACKEND", "FastAPI<br/>SQLAlchemy<br/>REST APIs"),
        ("DATA", "PostgreSQL<br/>Alembic"),
        ("TOOLS", "Git<br/>GitHub<br/>Docker<br/>Docker Compose"),
        ("PAYMENTS", "Razorpay<br/>Test-mode checkout"),
        ("ONLINE", "<font color='#0284C7'><b>LinkedIn</b></font><br/><font color='#0284C7'><b>GitHub</b></font>"),
        ("EDUCATION", "<b>Ganga Institute of<br/>Technology and Management</b><br/>Bachelor of Computer Applications (BCA)<br/>Expected 2027")
    ]
    for label, val in stacks:
        right_flow.append(Paragraph(label, style_stack_label))
        right_flow.append(Spacer(1, 1))
        right_flow.append(Paragraph(val, style_stack_val))
        right_flow.append(Spacer(1, 4))

    two_col_table = Table([[left_flow, right_flow]], colWidths=[380, 160])
    two_col_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (0,0), 14),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('LINELEFT', (1,0), (1,0), 0.75, colors.HexColor("#E2E8F0")),
    ]))
    story.append(two_col_table)
    story.append(Spacer(1, 6))

    # Page 1 Footer
    p1_footer = Table([[Paragraph("", style_normal), Paragraph("01 / 02", ParagraphStyle('P1Num', fontName='Helvetica', fontSize=7.5, textColor=TEXT_MUTED, alignment=2))]], colWidths=[450, 90])
    p1_footer.setStyle(TableStyle([('PADDING', (0,0), (-1,-1), 0)]))
    story.append(p1_footer)

    # ═════════════════════════════════════════════
    # PAGE 2
    # ═════════════════════════════════════════════
    story.append(PageBreak())

    # Header Page 2
    p2_top = [
        Paragraph("<font color='#0284C7'><b>KUSHANT / ENGINEERING PROFILE</b></font>", ParagraphStyle('P2Top', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=CYAN)),
        Spacer(1, 2),
        Paragraph("BUILDING PRODUCTS, NOT JUST PAGES.", ParagraphStyle('P2Title', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=NAVY)),
        Spacer(1, 2),
        Paragraph("A closer look at the engineering decisions represented by the NOVA project.", style_muted)
    ]
    for item in p2_top:
        story.append(item)
    story.append(Spacer(1, 8))

    # 3 Callout Cards
    box1 = [Paragraph("<b>FULL STACK</b>", style_stack_label), Paragraph("React + FastAPI<br/>+ PostgreSQL", style_normal)]
    box2 = [Paragraph("<b>SECURITY</b>", style_stack_label), Paragraph("Auth + rate limits<br/>+ reset flows", style_normal)]
    box3 = [Paragraph("<b>COMMERCE</b>", style_stack_label), Paragraph("Cart + orders<br/>+ payments", style_normal)]
    
    callouts_table = Table([[box1, box2, box3]], colWidths=[175, 175, 175])
    callouts_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_BOX),
        ('PADDING', (0,0), (-1,-1), 7),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_BOX),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(callouts_table)
    story.append(Spacer(1, 10))

    # 03 Engineering Capabilities
    story.append(Paragraph("03 ENGINEERING CAPABILITIES", style_sec_title))
    story.append(Spacer(1, 5))

    cap1 = [Paragraph("<b>FRONTEND ENGINEERING</b>", style_stack_label), Paragraph("Reusable React UI, route-based pages, client state and responsive Tailwind styling.", style_muted)]
    cap2 = [Paragraph("<b>API DEVELOPMENT</b>", style_stack_label), Paragraph("FastAPI endpoints with validation, authentication and clear separation of application concerns.", style_muted)]
    cap3 = [Paragraph("<b>DATABASE DESIGN</b>", style_stack_label), Paragraph("SQLAlchemy models and Alembic migrations for users, products, variants, carts, orders and payments.", style_muted)]
    cap4 = [Paragraph("<b>AUTH & SECURITY</b>", style_stack_label), Paragraph("JWT authentication, password hashing, reset flows and database-backed rate limiting.", style_muted)]
    cap5 = [Paragraph("<b>PAYMENT WORKFLOWS</b>", style_stack_label), Paragraph("Razorpay sandbox checkout, server-side order creation, payment events, webhooks and stock checks.", style_muted)]
    cap6 = [Paragraph("<b>LOCAL INFRASTRUCTURE</b>", style_stack_label), Paragraph("Docker Compose services for PostgreSQL and Mailpit, supporting repeatable local testing.", style_muted)]

    caps_table = Table([[cap1, cap2, cap3], [cap4, cap5, cap6]], colWidths=[175, 175, 175])
    caps_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 5),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FAFAFA")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
    ]))
    story.append(caps_table)
    story.append(Spacer(1, 10))

    # 04 Selected Nova Features (Table)
    story.append(Paragraph("04 SELECTED NOVA FEATURES", style_sec_title))
    story.append(Spacer(1, 4))

    feat_data = [
        [Paragraph("<b>Shopping experience</b>", style_normal), Paragraph("Product discovery, product details, saved items, cart and checkout flows.", style_muted)],
        [Paragraph("<b>Accounts</b>", style_normal), Paragraph("Registration, login, account management, password recovery and secure reset workflow.", style_muted)],
        [Paragraph("<b>Orders</b>", style_normal), Paragraph("Order confirmation, history and detail pages backed by relational order records.", style_muted)],
        [Paragraph("<b>Commerce logic</b>", style_normal), Paragraph("Product variants, stock validation, order item snapshots and payment-event tracking.", style_muted)],
        [Paragraph("<b>Developer environment</b>", style_normal), Paragraph("Docker Compose, PostgreSQL, Mailpit, Git/GitHub and environment-based configuration.", style_muted)],
        [Paragraph("<b>Deployment direction</b>", style_normal), Paragraph("Structured frontend/backend separation suitable for independent API and frontend deployment.", style_muted)]
    ]
    feat_table = Table(feat_data, colWidths=[140, 400])
    feat_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 2.5),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#F1F5F9")),
    ]))
    story.append(feat_table)
    story.append(Spacer(1, 8))

    # 05 Professional Profile
    story.append(Paragraph("05 PROFESSIONAL PROFILE", style_sec_title))
    story.append(Spacer(1, 3))
    prof_bullets = [
        "• <b>Strongest working style:</b> learn by building, validate ideas through working software, and improve architecture as product requirements become more realistic.",
        "• <b>Full-stack cohesion:</b> comfortable moving across frontend, backend and database layers instead of treating them as separate disciplines.",
        "• <b>Current career direction:</b> software development roles where practical full-stack ownership, problem solving and product-oriented engineering are valued."
    ]
    for b in prof_bullets:
        story.append(Paragraph(b, style_bullet))
        story.append(Spacer(1, 2.5))
    story.append(Spacer(1, 6))

    # 06 Developer Focus (3 columns)
    story.append(Paragraph("06 DEVELOPER FOCUS", style_sec_title))
    story.append(Spacer(1, 4))

    foc1 = [Paragraph("<b>BUILD</b>", style_stack_label), Paragraph("Turn ideas into working web products with clear user flows and reusable components.", style_muted)]
    foc2 = [Paragraph("<b>LEARN</b>", style_stack_label), Paragraph("Grow through practical projects, debugging, iteration and deeper backend understanding.", style_muted)]
    foc3 = [Paragraph("<b>OWN</b>", style_stack_label), Paragraph("Comfortably work across UI, API, database and development environment when a feature requires it.", style_muted)]
    
    focus_table = Table([[foc1, foc2, foc3]], colWidths=[175, 175, 175])
    focus_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (0,0), (-1,-1), BG_BOX),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_BOX),
    ]))
    story.append(focus_table)
    story.append(Spacer(1, 10))

    # Bottom Education & Connect Bar
    bot_edu = [
        Paragraph("<b>EDUCATION</b>", style_stack_label),
        Paragraph("<b>Ganga Institute of Technology and Management</b><br/>BCA • Expected Graduation 2027", style_muted)
    ]
    bot_conn = [
        Paragraph("<b>CONNECT</b>", style_stack_label),
        Paragraph("<font color='#0284C7'><b>linkedin.com/in/developerkushant</b></font><br/><font color='#0284C7'><b>github.com/honestlygolu</b></font>", style_muted)
    ]
    bot_table = Table([[bot_edu, bot_conn]], colWidths=[270, 270])
    bot_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0B1727")),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    # Text colors inside navy box for bot_table
    bot_edu_dark = [
        Paragraph("<b>EDUCATION</b>", ParagraphStyle('BE', fontName='Helvetica-Bold', fontSize=7, textColor=LIGHT_CYAN)),
        Paragraph("<b>Ganga Institute of Technology and Management</b><br/>BCA • Expected Graduation 2027", ParagraphStyle('BE2', fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=WHITE))
    ]
    bot_conn_dark = [
        Paragraph("<b>CONNECT</b>", ParagraphStyle('BC', fontName='Helvetica-Bold', fontSize=7, textColor=LIGHT_CYAN)),
        Paragraph("<font color='#38BDF8'><b>linkedin.com/in/developerkushant</b></font><br/><font color='#38BDF8'><b>github.com/honestlygolu</b></font>", ParagraphStyle('BC2', fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=WHITE))
    ]
    bot_table = Table([[bot_edu_dark, bot_conn_dark]], colWidths=[270, 270])
    bot_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(bot_table)
    story.append(Spacer(1, 6))

    # Page 2 Footer
    p2_footer = Table([[Paragraph("", style_normal), Paragraph("02 / 02", ParagraphStyle('P2Num', fontName='Helvetica', fontSize=7.5, textColor=TEXT_MUTED, alignment=2))]], colWidths=[450, 90])
    p2_footer.setStyle(TableStyle([('PADDING', (0,0), (-1,-1), 0)]))
    story.append(p2_footer)

    doc.build(story)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_pdf("resume.pdf")
