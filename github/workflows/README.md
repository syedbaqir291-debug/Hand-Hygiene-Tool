# 🧴 OMAC Hand Hygiene Tool
**By S M Baqir** — WHO 6-Step Hand Hygiene Assessment & Training System

A professional, AI-powered hand hygiene monitoring tool using MediaPipe hand skeleton tracking to teach and assess the WHO 6-step hand hygiene protocol.

---

## ✨ Features

- **Real-time hand skeleton tracking** — glowing joint-and-bone network via MediaPipe
- **WHO 6-Step detection** — automated gesture recognition for each step
- **Pass / Fail scoring** — green for correct, red for failed steps
- **3-second hold detection** — must hold correct posture for 3s to pass
- **Progress bar** — live visual of session completion
- **Dark / Light theme** — premium toggle
- **User login** — name, employee code, department
- **Excel export** — full session log with timestamps saved to `/results/`
- **Session log** — timestamped event stream

---

## 🚀 Quick Start

### Option A — GitHub Pages (static HTML)
1. Fork this repo
2. Go to **Settings → Pages** → Source: `main` / `root`
3. Visit `https://yourusername.github.io/omac-hand-hygiene/`

### Option B — Streamlit (with server-side Excel logging)
```bash
git clone https://github.com/yourusername/omac-hand-hygiene
cd omac-hand-hygiene
pip install -r requirements.txt
streamlit run app.py
```

---

## 📋 WHO 6-Step Protocol

| Step | Name | Description |
|------|------|-------------|
| 1 | Palm to Palm | Rub palms together in circular motion |
| 2 | Interlaced Fingers | Interlace fingers, rub between them |
| 3 | Back of Fingers | Right palm over left dorsum, fingers interlaced |
| 4 | Rotational Thumbs | Rotational rubbing of left thumb in right palm |
| 5 | Fingertip Scrub | Rotational rubbing of fingertips on left palm |
| 6 | Wrist Rotation | Rotate right wrist with left hand clasped |

---

## 📁 Project Structure
```
omac-hand-hygiene/
├── index.html          # Main tool (standalone, works on GitHub Pages)
├── app.py              # Streamlit launcher with server-side logging
├── requirements.txt    # Python dependencies
├── results/            # Auto-created; Excel logs saved here
└── README.md
```

---

## 🧠 Technology
- **MediaPipe Hands** — Google's hand landmark detection (21 keypoints)
- **Custom skeleton renderer** — canvas-based glowing joint network
- **SheetJS (xlsx.js)** — client-side Excel export
- **Streamlit** — optional Python server for centralized logging

---

## 📝 License
Developed by **S M Baqir** for OMAC. For institutional and training use.
