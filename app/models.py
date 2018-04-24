from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from app import db
from app import login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	user_id = db.Column(db.Integer, primary_key=True, nullable=False)
	username = db.Column(db.String(50), unique=True, nullable=False)
	email = db.Column(db.String(100))
	pass_hash = db.Column(db.String(128))

	def __repr__(self):
		return "<User {}>".format(self.username)

	def set_pass(self, password):
		self.pass_hash = generate_password_hash(password)

	def check_pass(self, password):
		return check_password_hash(self.pass_hash, password)

class Post(db.Model):
	post_id = db.Column(db.Integer, primary_key=True, nullable=False)
	title = db.Column(db.String(50))
	body = db.Column(db.String(200))
	user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))

	def __repr__(self):
		return "<Post: {} authoured by {}>".format(self.title, self.user_id)
