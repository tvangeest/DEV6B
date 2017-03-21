"""
Routes and views for the flask application.
"""

from flask import Flask, url_for
from development6b import app

@app.route('/')
def index():
   #return render_temlate('index.html')
   return