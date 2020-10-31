from flask import render_template, request, redirect, url_for,abort
from . import main
from ..request import get_quotes
from .forms import BlogForm, UpdateProfile
from .. import db
from ..models import Quote, Blog, User
from flask_login import login_required

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    title = 'Home '
    return render_template('index.html', title = title, quote = quotes)

@main.route('/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        new_blog = Blog(text = blog)
        # new_blog.save_blog()
        return redirect(url_for('main.index'))

    title = 'blog'
    return render_template('opinion.html',title = title, blog_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    