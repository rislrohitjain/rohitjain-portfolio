import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

# Initialize and map variables out of local .env file
load_dotenv()

# Safe environment metrics string parser
def parse_env_stats(env_name, default_str):
    raw_str = os.getenv(env_name, default_str)
    parsed = []
    try:
        for pair in raw_str.split(','):
            if ':' in pair:
                lbl, val = pair.split(':', 1)
                parsed.append({"label": lbl.strip().replace('_', ' '), "value": int(val.strip())})
    except Exception:
        pass
    return parsed

app = Flask(__name__)

# Decoupled Configuration Engine Map
app.config.update(
    BRAND_NAME=os.getenv("BRAND_NAME", "Rohit Jain"),
    INITIALS=os.getenv("INITIALS", "RJ"),
    PROFILE_PIC=os.getenv("PROFILE_PIC_FILENAME", "Rohit_Photo.jpg"),
    INTRO_VIDEO=os.getenv("INTRO_VIDEO_FILENAME", "add_my_profile_pic_or_video_wh.mp4"),
    FAVICON=os.getenv("FAVICON_FILENAME", "Rohit_Photo.jpg"),
    PROFILE={
        "title_sub": os.getenv("TITLE_SUB"),
        "name_first": os.getenv("NAME_FIRST"),
        "name_last": os.getenv("NAME_LAST"),
        "bio": os.getenv("BIO"),
        "location": os.getenv("LOCATION"),
        "open_to": os.getenv("OPEN_TO"),
        "email": os.getenv("EMAIL"),
        "phone": os.getenv("PHONE"),
    },
    GATEWAYS={
        "linkedin": os.getenv("LINKEDIN_URL"),
        "github": os.getenv("GITHUB_URL"),
        "live_portal": os.getenv("LIVE_PORTAL_URL"),
        "resume": os.getenv("RESUME_DOWNLOAD_URL"),
    },
    STATS={
        "languages": parse_env_stats("STATS_LANGUAGES", "Python:90,PHP:90,JavaScript:85,SQL:95,CSharp:65"),
        "domains": parse_env_stats("STATS_DOMAINS", "Backend:95,AI_Automation:90,Database:90,Security_API:85,Frontend:70"),
        "projects_count": parse_env_stats("STATS_PROJECTS_COUNT", "State_Platforms:12,AI_Applications:8,API_Middleware:8,E_Commerce:15")
    }
)

# Core Professional Timeline Dataset
EXPERIENCE_TIMELINE = [
    {
        "period": "April 2024 — Present",
        "company": "Data Ingenious Global Limited",
        "role": "Senior Software Developer (Jaipur)",
        "highlights": [
            "Architected and owned full SDLC for a mission-critical admission platform serving 100,000+ candidates across Regular and On-Demand Examination (ODE) streams.",
            "Engineered automated seat-allotment and result-generation modules using Laravel + MySQL, cutting processing time by 40% versus the legacy system.",
            "Implemented Role-Based Access Control (RBAC) covering 15+ user roles, reducing unauthorized access incidents to zero post-deployment.",
            "Deployed local-first AI code-assistance using Ollama, decreasing manual code-review cycles by 30% and accelerating sprint velocity.",
            "Spearheaded integration of Google Gemini and Claude APIs into developer tooling (VS Code + Antigravity), reducing debugging time by an estimated 25%.",
            "Piloting Agentic AI workflows (n8n, LangChain) and .NET Core Web API to expand platform capabilities into microservice architecture."
        ]
    },
    {
        "period": "February 2020 — April 2024",
        "company": "DevIT Solutions Pvt. Ltd.",
        "role": "Software Developer (Ahmedabad)",
        "highlights": [
            "Designed and delivered large-scale government web portals and e-commerce systems, serving 50,000+ daily users across Rajasthan state departments.",
            "Secured 50,000+ daily API calls for High Court and E-Court integrations using AES encryption and token-based authentication with zero data-breach incidents.",
            "Reduced RSOS result-generation time by 50% by rewriting batch processes as optimized MySQL stored procedures.",
            "Built seat-matrix algorithm for Paramedical Council multi-round counselling, handling category-wise allotments across 200+ colleges with 99.9% accuracy.",
            "Designed Pentaho and Tableau BI dashboards for technical education departments, enabling real-time drill-down reporting for 10+ KPIs."
        ]
    },
    {
        "period": "October 2017 — January 2020",
        "company": "Akal Information Systems Ltd.",
        "role": "Software Developer (Delhi)",
        "highlights": [
            "Developed and maintained enterprise web applications for government and corporate clients.",
            "Contributed heavily to core API system integrations and targeted database structural optimization projects.",
            "Collaborated with cross-functional product teams to deliver secure, high-availability applications within aggressive timelines."
        ]
    },
    {
        "period": "August 2016 — October 2017",
        "company": "Vertex Plus Software Pvt. Ltd.",
        "role": "Junior Software Developer (Jaipur)",
        "highlights": [
            "Built clean, responsive web applications and secure client portals using PHP, jQuery, and Bootstrap modules.",
            "Gained first structural exposure to complex SOAP/REST API consumption layers and system modeling."
        ]
    },
    {
        "period": "December 2015 — August 2016",
        "company": "On-Graph Technologies Pvt. Ltd.",
        "role": "Junior Developer (Jaipur)",
        "highlights": [
            "Developed robust CMS-driven websites and active horizontal community portals.",
            "Successfully integrated SMS gateway infrastructure alongside real-time notification engine systems."
        ]
    }
]

# Core Enterprise Project Highlights Dataset
PROJECT_HIGHLIGHTS = [
    {
        "category": "Python AI & Agentic Workflows",
        "title": "Python AI Suite & Autonomous Agents",
        "desc": "Designed and deployed Python-based AI applications utilizing Ollama, LangChain, Google Gemini API, and Anthropic Claude. Features automated code review, RAG document processing, and autonomous workflow automation pipelines."
    },
    {
        "category": "State Platform Architecture",
        "title": "RSOS Student Lifecycle Portal",
        "desc": "End-to-end platform managing Admission → Examination → Result Publishing. Integrated natively with Rajasthan SSO. Achieved a 50% runtime reduction in lifecycle generation through explicit stored-procedure refinement optimizations."
    },
    {
        "category": "Middleware Encryption Security",
        "title": "High Court & E-Court API",
        "desc": "Secured over 50,000+ daily API transactions using customized cryptographic AES encryption/decryption middleware. Zero safety incidents reported since launch; subsequently adopted as standard for two alternative GOR departments."
    },
    {
        "category": "State-Wide Resource Tracking",
        "title": "IT Job Fair Portal",
        "desc": "Multi-location platform orchestration layer facilitating state candidate/company registration workflows, real-time vacancy capacity tracking updates, and automated, AI-assisted candidate profiling shortlists."
    },
    {
        "category": "Privacy-First Engineering",
        "title": "Local LLM Development Cluster",
        "desc": "Isolated secure LLM cluster deployment running Ollama, Gemini, and Claude parameters for automated system review tasks. Cut manual source validation workloads by 30%; currently driving automated test engine generation models."
    }
]

# Comprehensive Skill-Set Structural Matrix Dictionary
TECHNICAL_MATRIX = {
    "Languages": ["Python (Advanced)", "PHP", "JavaScript", "SQL", "C# / .NET"],
    "Frameworks & CMS": ["Laravel", "Flask", "FastAPI", "CakePHP", "jQuery", "Bootstrap", "Core .NET", "WordPress"],
    "AI & LLM Integration": ["Python Agentic AI", "Ollama (Local/Cloud)", "Google Gemini API", "Claude (Anthropic)", "n8n Workflow Hub", "LangChain", "RAG Systems", "AI-IVR Systems"],
    "Databases & Analytics": ["MySQL", "MSSQL", "PostgreSQL", "ChromaDB (Vector DB)", "Pentaho BI", "Tableau"],
    "Architecture & DevOps": ["REST/SOAP APIs", "RBAC Security", "Microservices", "Git / GitHub", "Docker", "IIS Server", "Vercel"]
}

# Tech Community & Tech Event Participation Dataset
COMMUNITY_EVENTS = [
    {
        "title": "BrowserStack Testathon Jaipur 2026",
        "date": "Saturday, September 5, 2026 | 10:00 AM IST",
        "location": "Metacube Software Pvt. Ltd., Sitapura Industrial Area, Jaipur, Rajasthan",
        "organizer": "BrowserStack Community",
        "badge": "QA & Test Automation",
        "highlights": [
            "3-Hour Hands-On Hackathon: Designed, documented, and developed an end-to-end automated test suite for a buggy web application under a 3-hour constraint.",
            "BrowserStack QA Suite Utilization: Leveraged BrowserStack Automate (cross-browser/device execution), Test Management, Test Companion, and Test Observability (failure pattern analysis).",
            "Framework & Code Integration: Integrated test automation frameworks (Selenium, Playwright, Cypress) using BrowserStack SDK and published repositories on GitHub."
        ]
    },
    {
        "title": "Cloud Coffee Connect — AI on AWS & Open Source",
        "date": "Saturday, September 19, 2026 | 10:00 AM – 1:00 PM IST",
        "location": "Pratham Software, Sitapura Industrial Area, Jaipur, Rajasthan",
        "organizer": "AWS User Group Jaipur",
        "badge": "AI & Cloud Architecture",
        "highlights": [
            "Cloud & AI Focus: Technical meetup focused on deploying, optimizing, and scaling Artificial Intelligence (AI) solutions on AWS alongside open-source AI frameworks.",
            "Architectural Discussions & Networking: Explored open-source LLMs, AI/ML pipelines on AWS, and interacted with cloud engineers, AI developers, and architects."
        ]
    },
    {
        "title": "Atlassian × Tableau: Integrating Jira & Confluence with Tableau",
        "date": "Sunday, September 20, 2026 | 11:00 AM – 2:00 PM IST",
        "location": "Kundan Hall, The Fern Jaipur, Tonk Road, Jaipur, Rajasthan",
        "organizer": "Atlassian Community Events",
        "badge": "DevOps & Data Analytics",
        "highlights": [
            "Integrating Jira & Confluence with Tableau (by Hemant Saini): Technical session on setting up architecture to connect Jira Cloud and Confluence with Tableau Server/Cloud (OAuth, SSO, PATs, live metrics embedding).",
            "Atlassian & Tableau Certifications: Insights into certification paths, exam structures, and learning pathways presented by Anamika Soni and Tarun Gupta.",
            "Community Engagement: Active participation in technical Q&A and community networking."
        ]
    },
    {
        "title": "Agile Testing Alliance (ATA)",
        "date": "August 28, 2026",
        "location": "Jaipur, Rajasthan",
        "organizer": "Agile Testing Alliance",
        "badge": "Agile Quality Engineering",
        "highlights": [
            "Agile QA & Testing Community: Participated in community learning and professional networking with industry leaders from Agile Testing Alliance.",
            "Core Themes: Focused on agile testing methodologies, test automation standards, continuous testing pipelines, and modern quality engineering practices."
        ]
    }
]

# Root Presentation Route Handler
@app.route('/')
def home():
    return render_template(
        'index.html',
        config=app.config,
        timeline=EXPERIENCE_TIMELINE,
        projects=PROJECT_HIGHLIGHTS,
        matrix=TECHNICAL_MATRIX,
        events=COMMUNITY_EVENTS
    )

# Dedicated Static Asset Delivery Route for Root-Level File Mapping
@app.route('/<filename>')
def serve_root_assets(filename):
    # Allows app.py to dynamically route files stored straight inside the root directory safely
    return send_from_directory('.', filename)

if __name__ == '__main__':
    # Binding port for Hugging Face or general container deployment infrastructure
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)