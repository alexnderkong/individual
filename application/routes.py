from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Posts, Users
from application.forms import PostForm, UsersForm, LoginForm, UpdateAccountForm, UpdatePokemonForm, SearchForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='about')
	#postData = Posts.query.all()
	#return render_template('home.html', title='home', posts=postData)

@app.route('/homeuser', methods=['POST','GET'])
@login_required
def homeuser():
	postData = Posts.query.all()

	form = SearchForm()
	if request.method == 'POST' and form.content.data == 'All':
		try:
			print("Alex")
			return redirect(url_for('homeuser'))
		except:
			return "not working"
	elif request.method == 'POST':
		
		try:
			print("Hello")
			postData = Posts.query.filter_by(content=form.content.data).all()
		except:
			return 'broken'
	return render_template('homeuser.html', title='Homeuser', homeuser=postData ,form=form)



@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('homeuser'))

	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('homeuser'))
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
	if form.validate_on_submit():
		postData=Posts(
			title=form.title.data,
			content=form.content.data,
			level=form.level.data,
			author=current_user
			)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('homeuser'))
	else:
		print(form.errors)
	return render_template('post.html', title='post', form=form)

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
		return redirect('/homeuser')
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
			return redirect('/homeuser')
		except:
			return 'An issue occurred'

	else:
		return render_template('update.html', form=form, post=post)