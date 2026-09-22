---
title: Rohitjain Portfolio
emoji: 💻
colorFrom: gray
colorTo: purple
sdk: docker
pinned: false
license: mit
short_description: rohitjain-portfolio
---

# 🚀 Rohit Jain — Portfolio & Interactive Analytics Dashboard

A modern, high-performance portfolio landing page and dynamic analytics dashboard built for **Rohit Jain** (Senior Full-Stack Developer & AI Automation Architect). Features custom glassmorphism design ("Aether Glow"), real-time Chart.js graphical metrics loaded from environment variables, local LLM & automated workflow highlights, embedded map location frame, and PDF resume viewer.

---

## 🌐 Live Deployments & Repository Links

* **🐙 GitHub Repository**: [https://github.com/rislrohitjain/rohitjain-portfolio](https://github.com/rislrohitjain/rohitjain-portfolio)
* **⚡ Vercel Live Deployment**: [https://rohitjain-resume.vercel.app/](https://rohitjain-resume.vercel.app/)
* **🤗 Hugging Face Space**: [https://huggingface.co/spaces/rislrohitjain/rohitjain-portfolio](https://huggingface.co/spaces/rislrohitjain/rohitjain-portfolio)

---

## ✨ Key Features & Architecture

1. **Aether Glow Visual Redesign**:
   - Modern geometric typography (**Outfit** headings paired with **Plus Jakarta Sans** body text).
   - Ambient floating neon background glow blobs (`driftBlob` animations).
   - Conic-gradient rotating profile ring with fallback initial avatars.
   - Glassmorphic translucent cards with 3D mouse-tracking tilt effects.

2. **Graphical Metrics & Analytics Dashboard**:
   - **Domain Core Strengths**: Radar capability map rendered via Chart.js.
   - **Language Stack**: Horizontal bar chart reflecting programming language proficiencies.
   - **Project Allocations**: Donut chart detailing category-wise project distribution.
   - **Dynamic `.env` Parsing**: All metrics and numbers load dynamically from environment variables.
   - **Numerical Count Badges**: Pill badges with exact percentages and project count metrics beneath each chart card.

3. **Responsive Navigation & Mobile Drawer**:
   - Glassmorphic top floating pill navbar tracking active scroll sections.
   - Fluid mobile navigation drawer overlay with z-index stacking.

4. **Media & Assets**:
   - Native HTML5 video player integration.
   - Built-in PDF resume viewer opening directly in a popup/new tab.
   - Responsive Google Maps frame integration.

---

## 🛠️ Tech Stack

* **Backend Framework**: Python 3.11 / Flask 3.0
* **Frontend**: HTML5, Modern CSS3 (CSS Grid, Flexbox, Glassmorphic Backdrop Filters), JavaScript (ES6+)
* **Data Visualization**: Chart.js 4.x
* **Containerization**: Docker
* **Deployment Targets**: Vercel (Serverless Python Builder `@vercel/python`), Hugging Face Spaces (Docker SDK), GitHub Pages / Web Hosting

---

## ⚙️ Environment Configuration (`.env`)

```env
# Branding & Profile Metadata
BRAND_NAME="Rohit Jain"
INITIALS="RJ"
TITLE_SUB="Senior Full-Stack Developer & AI Automation Architect"
NAME_FIRST="Rohit"
NAME_LAST="Jain"
BIO="Delivering resilient government portal engineering, secure API architectures, and localized, privacy-first enterprise automation loops."
LOCATION="Jaipur, Rajasthan"
OPEN_TO="Remote, Hybrid, Relocation"

# Communication & Links
EMAIL="engrohitjain5@gmail.com"
PHONE="+91 89469 19241"
LINKEDIN_URL="https://linkedin.com/in/rohit-jain-061571a3"
GITHUB_URL="https://github.com/rislrohitjain/rohitjain-portfolio"
LIVE_PORTAL_URL="https://rohitjain-resume.vercel.app/"
RESUME_DOWNLOAD_URL="/Rohit_Jain_Resume.pdf"

# Media File Asset Mappings
PROFILE_PIC_FILENAME="Rohit_Photo.jpg"
INTRO_VIDEO_FILENAME="add_my_profile_pic_or_video_wh.mp4"
FAVICON_FILENAME="Rohit_Photo.jpg"

# Graphical Analytics Parameters
STATS_LANGUAGES="PHP:90,JavaScript:85,SQL:95,Python:70,CSharp:65"
STATS_DOMAINS="Backend:95,Database:90,AI_Automation:80,Security_API:85,Frontend:70"
STATS_PROJECTS_COUNT="State_Platforms:12,API_Middleware:8,AI_Tools:5,E_Commerce:15"
```

---

## 💻 Local Quickstart

### Prerequisites
- Python 3.9+
- Git & Git LFS (for large media handling)

### 1. Clone the Repository
```bash
git clone https://github.com/rislrohitjain/rohitjain-portfolio.git
cd rohitjain-portfolio
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

### 3. Run the Development Server
```bash
python app.py
```

The application will bind to `0.0.0.0:7860` and can be accessed at:
- **Localhost**: `http://127.0.0.1:7860`
- **Local Network IP**: `http://<YOUR_LOCAL_IP>:7860` (e.g. `http://172.18.177.164:7860`)

---

## 📦 Deployment Guides

### Vercel Serverless Deployment
The repository includes a root `vercel.json` configured for serverless Python builds:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```
Simply connect your GitHub repository `rislrohitjain/rohitjain-portfolio` on the [Vercel Dashboard](https://vercel.com/) and deploy.

### Hugging Face Space (Docker)
The repository includes a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
ENV PORT=7860
CMD ["python", "app.py"]
```
Push the code to your Hugging Face Space remote:
```bash
git remote add hf https://huggingface.co/spaces/rislrohitjain/rohitjain-portfolio
git push hf main
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
