from fpdf import FPDF

# Replace problematic em dash with standard hyphen
def sanitize_text(text):
    return text.replace("—", "-")

# Custom PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Prajyot Pating More", ln=True, align="C")
        self.set_font("Arial", "", 11)
        self.cell(0, 10, "Aspiring Strategy, Finance, and Technology Consultant | IIT Kharagpur", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(1)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.set_text_color(50)
        self.multi_cell(0, 8, sanitize_text(body))
        self.ln()

# Create PDF
pdf = PDF()
pdf.add_page()

# Education
pdf.chapter_title("EDUCATION")
pdf.chapter_body("""
IIT Kharagpur - B.S. in Applied Geology (Expected Graduation: 2028)
- Strong foundation in problem-solving, analytics, and scientific thinking.
- Actively self-learning Finance, Consulting, AI/ML, and Backend Development.
""")

# Strategy/Consulting Experience
pdf.chapter_title("STRATEGY & CONSULTING EXPERIENCE")
pdf.chapter_body("""
Outreach Coordinator - Global Entrepreneurship Summit, IIT KGP
- Reached out to 200+ startup founders and CEOs to collaborate with GES.
- Strategically negotiated and confirmed multiple speaker slots and sponsorships.
- Coordinated outreach pipelines and ensured high-response follow-up communication.

Finance & AI Startup Research - Self-driven
- Conducted financial & product analysis of multiple AI startups in bond markets and analytics.
- Built a full-stack bond information API solution for hackathons.

Content Creation Strategy - Twitter, LinkedIn, YouTube
- Publicly building a personal brand by documenting my journey in AI, tech, and finance.
- Researched successful content & engagement strategies to optimize short-form video creation.
""")

# Technical Skills
pdf.chapter_title("TECHNICAL SKILLS")
pdf.chapter_body("""
- Programming: Python, C++, SQL, JavaScript (Basics)
- AI/ML: NumPy, Pandas, scikit-learn, Matplotlib, Deep Learning Specialization (in progress)
- Backend: Node.js (ongoing), Express, MongoDB (planned)
- Tools: Git, GitHub, VS Code, DaVinci Resolve, Notion, Streamlit
""")

# Projects
pdf.chapter_title("SELECTED PROJECTS")
pdf.chapter_body("""
Linear Regression Web App
- Built using Python and Streamlit to predict marks from study hours; deployed via GitHub.

YouTube Shorts Automation Strategy
- Created automated Python + DaVinci Resolve editing templates to streamline YouTube Shorts based on coding journey.

Hackathon Bond Analytics Platform (Concept)
- Built ISIN lookup, bond search, comparison, and risk analytics modules as part of a full-stack design challenge.
""")

# Extracurricular & Leadership
pdf.chapter_title("EXTRACURRICULAR & INITIATIVES")
pdf.chapter_body("""
- Member, Computer Graphics & Game Dev Society - IIT KGP
- Actively involved in coding clubs and peer tech discussions.
- Regular participant in AI/ML hackathons and Twitter communities.
""")

# Save PDF
pdf_output_path = "/mnt/data/Prajyot_More_Consulting_Resume.pdf"
pdf.output(pdf_output_path)

pdf_output_path