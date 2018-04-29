from app import app, db
from app.models import User, Post
from config import version

print("\n\n" + "-" * 25)
print('Starting Techbench server')
print('Version:', version)
print("-" * 25 + "\n\n")


@app.shell_context_processor
def make_shell_context():
	return {
		'db': db,
		'User': User,
		'Post': Post
	}
