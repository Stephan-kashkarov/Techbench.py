import os
basedir = os.path.abspath(os.path.dirname(__file__))

version = "0.1/py"

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'work-is-for-the-weak!'

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
