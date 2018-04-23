from flask import render_template, flash, redirect, url_for, request
from app import app
from config import version

@app.route('/')
@app.route('/main')
def main():
	return render_template('main.html', version=version)
