#! /usr/bin/python3
"""
web frontend for SQL Queries of a backend database
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    """
    example pulled from flask docs
    """
    return render_template('does_not_exsist.html'), 404


@app.route('/')
def index():
    """
    defines a page
    """
    return render_template('index.html')


@app.route("/scanner", methods=['get'])
def results():
    """
    defines a page
    """
    return render_template("scanner.html")


@app.route("/scan_results", methods=['get', 'post'])
def scan():
    """
    defines a page
    """
    target = '127.0.0.1'
    s_port = "1"
    e_port = "1234"
    ports = ["22 open", "80 closed"]
    if request.method == 'POST':
        target = request.form['target']
        s_port = request.form['s_port']
        e_port = request.form['e_port']
        return render_template("scan_results.html", target=target, s_port=s_port, e_port=e_port, ports=ports)
    results = None
    return render_template("scanner.html", combatants=results)

if __name__ == "__main__":
    app.run(debug=True, port=8050)