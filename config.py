import os
basedir = os.path.abspath(os.path.dirname(__file__))

version = "0.1/py"

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'work-is-for-the-weak!'
