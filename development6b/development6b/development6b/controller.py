from flask import Flask, render_template

class Controller:
  #index
  def index():
    return render_template('index.html')