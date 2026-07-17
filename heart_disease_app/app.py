from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Tableau view configuration
# ---------------------------------------------------------------------------
# Replace these with the "Embed Code" URLs from your published Tableau Public
# workbook (Share -> Embed Code). Format is typically:
#   https://public.tableau.com/views/<WorkbookName>/<ViewName>
# ---------------------------------------------------------------------------
TABLEAU_VIEWS = {
    "dashboard": {
        "title": "Heart Disease Risk Dashboard",
        "description": "Interactive dashboard exploring key risk factors, "
                        "prevalence trends, and demographic breakdowns for heart disease.",
        "url": "https://prod-in-a.online.tableau.com/t/udayv588-6a6048d974/views/HeartDiseasedashboard/Dashboard3",
        "height": "840px",
    },
    "story": {
        "title": "Heart Disease Insights Story",
        "description": "A guided narrative walking through the data — from risk "
                        "factors to outcomes — for healthcare professionals and policymakers.",
        "url": "https://prod-in-a.online.tableau.com/t/udayv588-6a6048d974/views/HeartDiseasedashboard/Story1",
        "height": "1004px",
    },
}

@app.route("/")
def home():
    return render_template("index.html", active="home")


@app.route("/about")
def about():
    return render_template("about.html", active="about")


@app.route("/dashboard")
def dashboard():
    view = TABLEAU_VIEWS["dashboard"]
    return render_template("viz.html", view=view, active="dashboard")


@app.route("/story")
def story():
    view = TABLEAU_VIEWS["story"]
    return render_template("viz.html", view=view, active="story")


@app.route("/contact")
def contact():
    return render_template("contact.html", active="contact")


if __name__ == "__main__":
    app.run(debug=True)
