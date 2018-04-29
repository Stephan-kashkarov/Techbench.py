from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import login_form, register_form
from app.models import User, Post
from config import version
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/main')
def main():
	return render_template('main.html', version=version)


@app.route('/login')
def login():
	if current_user.is_authenticated:
		flash('You are already logged in!')
		return redirect(url_for('home'))
	Form = login_form
	if Form.validate_on_submit():
		user = User.query.filter_by(username=Form.username.data).first()
		if user is None or not user.check_password_hash(Form.password.data):
			flash('invalid username or password!')
		login_user(user, remember=Form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			return redirect(url_for('home'))
		return redirect(next_page)
	return render_template('index.html', form=Form)


@app.route('/logout')
def logout():
	login_user()
	return redirect(url_for('home'))


@app.route('/register')
def register():
	if current_user.is_authenticated:
		flash('You are already logged in, You dont need to register!')
		return redirect(url_for('home'))
	Form = register_form
	if Form.validate_on_submit():
		u = User(username=form.username.data, email=form.email.data)
		u.set_pass(form.password.data)
		db.session.add(u)
		db.session.commit()
		flash("User {} is now registered, Congrats!".format(form.username.data))
		return url_for("login")
	return render_template("regester.html", form=Form)
