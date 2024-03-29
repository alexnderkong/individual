from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, UsersForm, LoginForm, UpdateAccountForm, UpdatePokemonForm, SearchForm
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
import os

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')
	#postData = Posts.query.all()
	#return render_template('home.html', title='home', posts=postData)

def save_picture(form_picture):
	picture_path = os.path.join(app.root_path, 'static', form_picture.filename)
	picture = form_picture.filename
	form_picture.save(picture_path)
	return picture


@app.route('/homeuser/<int:user_id>', methods=['POST','GET'])
@login_required
def homeuser(user_id):
	posts = Posts.query.filter_by(user_id=user_id)
	if current_user.id != user_id:
		return redirect(url_for('home'))
	else:	
		user = Users.query.get_or_404(user_id)
		postData = Posts.query.filter_by(user_id=user_id)

	form = SearchForm()
	if request.method == 'POST' and form.content.data == 'All':
		try:
			print("Alex")
			return redirect(url_for('homeuser', user_id=current_user.id))
		except:
			return "not working"
	elif request.method == 'POST':
		
		try:
			print("Hello")
			postData = Posts.query.filter_by(content=form.content.data, user_id=current_user.id).all()
		except:
			return 'broken'
	return render_template('homeuser.html', title='Homeuser', homeuser=postData ,form=form)



@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('homeuser', user_id=current_user.id))

	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('homeuser', user_id=current_user.id))
	return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = UsersForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user=Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data,
			password=hashed_pw
			)

		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='register', form=form)

@app.route('/post', methods=['GET','POST'])
@login_required
def post():
	form=PostForm()
	image_file = url_for('static', filename='default.png')
	if form.validate_on_submit():
		if form.picture.data:
			picture_path = save_picture(form.picture.data)
			full_path = '/static/' + picture_path
			postData=Posts(
				title=form.title.data,
				content=form.content.data,
				level=form.level.data,
				author=current_user,
				image_file=full_path
				)
			db.session.add(postData)
			db.session.commit()
			image_file = url_for('static', filename=picture_path)
			return redirect(url_for('homeuser', user_id=current_user.id))
		else:
			postData=Posts(
				title=form.title.data,
				content=form.content.data,
				level=form.level.data,
				author=current_user,
				image_file='/static/default.png'
				)
			db.session.add(postData)
			db.session.commit()
			return redirect(url_for('homeuser', user_id=current_user.id))
	else:
		print(form.errors)
	return render_template('post.html', title='Add Pokemon', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account',form=form)

@app.route('/delete/<int:id>')
def delete(id):
	pokemon_to_delete = Posts.query.get_or_404(id)
	try:
		db.session.delete(pokemon_to_delete)
		db.session.commit()
		return redirect(url_for('homeuser', user_id=current_user.id))
	except:
		return 'An issue occurred'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
	form = UpdatePokemonForm()
	post = Posts.query.get_or_404(id)
	if request.method == 'POST':
		post.level = request.form['level']
		try:
			db.session.commit()
			return redirect(url_for('homeuser', user_id=current_user.id))
		except:
			return 'An issue occurred'

	else:
		return render_template('update.html', form=form, post=post)

@app.route('/user/delete/<int:user_id>', methods=['GET','POST'])
@login_required
def delete_user(user_id):
	user = Users.query.get_or_404(user_id)
	post = Posts.query.filter_by(user_id=user_id).all()
	if user:
		for i in post:
			db.session.delete(i)
		db.session.delete(user)
		db.session.commit()
		return redirect(url_for('logout'))
	else:
		return'Error occurred'