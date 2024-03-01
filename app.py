import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from helpers import apology, login_required, lookup
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.route("/")
def index():
    """Show Index File"""
    return render_template("index.html")

@app.route('/about')
def about():
    """Show About File"""
    return render_template("about.html")

@app.route('/contact')
def contact():
    """Show Contact File"""
    return render_template("contact.html")

@app.route('/clicktostart')
def click_to_start():
    """Show Click to Start File"""
    return render_template("clicktostart.html")

@app.route('/whatamiautomotive')
def what_am_i_automotive():
    """Show What am I Automotive File"""
    return render_template("whatamiautomotive.html")

@app.route('/whatamielectricalins')
def what_am_i_electricalins():
    """Show What am I Electricalins File"""
    return render_template("whatamielectricalins.html")

@app.route('/whatamielectricaleng')
def what_am_i_electricaleng():
    """Show What am I Electricaleng File"""
    return render_template("whatamielectricaleng.html")

@app.route('/whatamimachining')
def what_am_i_machining():
    """Show What am I Machining File"""
    return render_template("whatamimachining.html")

@app.route('/whatamiconstruction')
def what_am_i_construction():
    """Show What am I Construction File"""
    return render_template("whatamiconstruction.html")

@app.route('/whatamivisual')
def what_am_i_visual():
    """Show What am I Visual File"""
    return render_template("whatamivisual.html")

@app.route('/whatamiusedforautomotive')
def what_am_i_used_for_automotive():
    """Show What am I Automotive File"""
    return render_template("whatamiusedforautomotive.html")

@app.route('/whatamiusedforelectricalins')
def what_am_i_used_for_electricalins():
    """Show What am I Electricalins File"""
    return render_template("whatamiusedforelectricalins.html")

@app.route('/whatamiusedforelectricaleng')
def what_am_i_used_for_electricaleng():
    """Show What am I Electricaleng File"""
    return render_template("whatamiusedforelectricaleng.html")

@app.route('/whatamiusedformachining')
def what_am_i_used_for_machining():
    """Show What am I Machining File"""
    return render_template("whatamiusedformachining.html")

@app.route('/whatamiusedforconstruction')
def what_am_i_used_for_construction():
    """Show What am I Construction File"""
    return render_template("whatamiusedforconstruction.html")

@app.route('/whatamiusedforvisual')
def what_am_i_used_for_visual():
    """Show What am I Visual File"""
    return render_template("whatamiusedforvisual.html")

@app.route('/trueorfalseautomotive')
def true_or_false_automotive():
    """Show True or False Automotive File"""
    return render_template("trueorfalseautomotive.html")

@app.route('/trueorfalseelectricalins')
def true_or_false_electricalins():
    """Show True or False Electricalins File"""
    return render_template("trueorfalseelectricalins.html")

@app.route('/trueorfalseelectricaleng')
def true_or_false_electricaleng():
    """Show True or False Electricaleng File"""
    return render_template("trueorfalseelectricaleng.html")

@app.route('/trueorfalsemachining')
def true_or_false_machining():
    """Show True or False Machining File"""
    return render_template("trueorfalsemachining.html")

@app.route('/trueorfalseconstruction')
def true_or_false_construction():
    """Show True or False Construction File"""
    return render_template("trueorfalseconstruction.html")

@app.route('/trueorfalsevisual')
def true_or_false_visual():
    """Show True or False Visual File"""
    return render_template("trueorfalsevisual.html")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/contact2', methods=["GET", "POST"])
def contact2():
    """dashboard pembimbing"""
    comment=db.execute("SELECT * FROM comment ORDER BY id_comment DESC LIMIT 2")
    if request.method == "POST":
        name = request.form.get("name")
        comment = request.form.get("comment")

        # Insert a new comment to database
        db.execute("INSERT INTO comment (name, comment) VALUES(?, ?)", name, comment)
        return redirect("/contact2")

    else:
        return render_template("contact.html", comments=comment)


