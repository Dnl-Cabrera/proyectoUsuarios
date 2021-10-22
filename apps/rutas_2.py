from app import app
from flask import render_template


@app.route('/adminUser')
def adminUser():
    return render_template("adminEmplo.html")