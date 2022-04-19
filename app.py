from flask import Flask, redirect, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
'''
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
'''

@app.route('/about.html')
def about():
    return render_template('/static/about.html')

@app.route('/project.html')
def project():
    return render_template('/static/project.html')