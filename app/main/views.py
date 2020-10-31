from flask import render_template, request, redirect, url_for,abort
from . import main
from ..request import get_quotes
from .forms import BlogForm
from ..models import Quote, Blog
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
