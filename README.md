# Assessment 2 Flask Web App

This is a simple, testable Flask project for **Assessment 2 — Build a Student Profile Page with Flask and HTML**.

## Project Structure

```text
assessment2_flask_webapp/
├── app.py
├── requirements.txt
├── static/
│   └── styles.css
└── templates/
    ├── base.html
    └── index.html
```

## How to Run

### 1. Open terminal in this folder

### 2. Create a virtual environment
```bash
python -m venv .venv
```

### 3. Activate it
#### Windows
```bash
.venv\Scripts\activate
```

#### macOS / Linux
```bash
source .venv/bin/activate
```

### 4. Install Flask
```bash
python -m pip install -r requirements.txt
```

### 5. Run the app
```bash
python app.py
```

### 6. Open in browser
Visit:
```text
http://127.0.0.1:5000
```

## What this app demonstrates
- Flask backend setup
- HTML template rendering with `render_template()`
- Multi-section student profile page
- Setup checklist section
- Ready-to-test localhost page
