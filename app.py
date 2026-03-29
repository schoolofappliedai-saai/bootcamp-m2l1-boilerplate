from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "student_name": "Aarav Sharma",
    "program_name": "Career Launchpad Basic Cohort",
    "why_python": (
        "I want to learn Python because it helps me build useful software quickly, "
        "understand backend logic, and start creating real web applications with AI-ready workflows."
    ),
    "lesson_takeaways": [
        "How to install Python and verify the version in the terminal.",
        "Why virtual environments matter and how to activate one.",
        "How Flask connects Python backend logic with HTML templates."
    ],
    "setup_status": (
        "My machine is now ready for beginner Python web development. "
        "Python is installed, pip is working, Flask is installed, and my app runs on localhost."
    ),
    "checklist": [
        {"item": "Python installed", "done": True},
        {"item": "pip working", "done": True},
        {"item": "virtual environment created", "done": True},
        {"item": "Flask installed", "done": True},
        {"item": "app running on localhost", "done": True},
    ],
}


@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE, page_title="Student Profile Page")


if __name__ == "__main__":
    app.run(debug=True)
