from flask import render_template, request, redirect, url_for,abort
from . import main
from ..request import get_quotes
from .forms import BlogForm
from ..models import Quote, Blog
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    quotes = get_quotes()
    # print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, quote = quotes)

@main.route('/blog', methods = ['GET','POST'])
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
