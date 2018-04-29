from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from app.models import User


class login_form(FlaskForm):
	"""Login form."""

	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Submit')


class register_form(FlaskForm):
	"""Regestration form."""

	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	pass1 = PasswordField('Password', validators=[DataRequired()])
	pass2 = PasswordField(
		'Confirm Password',
		validators=[DataRequired(), EqualTo(pass1)])
	submit = SubmitField('Submit')

	def validate_name(self, name):
		"""Validator for username."""
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError("Username already Taken")

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email is not None:
			raise ValidationError("Email already taken")
