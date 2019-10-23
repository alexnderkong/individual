from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200),nullable=False)
	content = db.Column(db.String(100),nullable=False)
	level = db.Column(db.Integer, nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	image_file = db.Column(db.String(50),nullable=False, default='default.png')

	user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join([
			'user: ', self.user_id, ' ', '\r\n', 
			'title: ', self.title, '\r\n', self.content
			 ])

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50),nullable=False)
	last_name = db.Column(db.String(50),nullable=False)
	email = db.Column(db.String(150),nullable=False,unique=True)
	password = db.Column(db.String(100),nullable=False)
	posts = db.relationship('Posts', backref='author', lazy=True)

	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 
			'Email: ', self.email, 'Name: ', self.first_name, ' ',self.last_name])

	@login_manager.user_loader
	def load_user(id):
		return Users.query.get(int(id))