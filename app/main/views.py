from flask import render_template, request, redirect, url_for,abort
from . import main
from ..request import get_quotes
from .forms import BlogForm, UpdateProfile, CommentForm
from .. import db, photos
from ..models import Quote, Blog, User, Comment
from flask_login import login_required, current_user

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    blogs = Blog.query.all()
    title = 'Home '
    return render_template('index.html', title = title, quote = quotes, blogs = blogs)

@main.route('/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        new_blog = Blog(text = blog, title = title, user=current_user)
        new_blog.save_blog()
        return redirect(url_for('main.index'))

    title = 'blog'
    return render_template('opinion.html',title = title, blog_form=form)

@main.route('/update_blog/<int:id>', methods=['GET', 'POST'])
@login_required
def update_blog(id):
    blog = Blog.query.get(id)
    if blog.user.id != current_user.id:
        abort(403)

    form = BlogForm()

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.text = form.blog.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('opinion.html', blog_form=form)

@main.route('/delete_blog/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.query.get(id)
    if blog.user.id != current_user.id:
        abort(403)
    db.session.delete(blog)
    db.session.commit()    
    return redirect (url_for('main.index'))    

@main.route('/view_comments/<id>')
@login_required
def view_comments(id):
    comment = Comment.get_comments(id)
    title = "View Comments"
    return render_template('comment.html', comment_list= comment, title=title)

@main.route('/comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def comment(blog_id):
    form= CommentForm()
    blog = Blog.query.filter_by(id= blog_id).first()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, user = current_user, blog_id = blog_id)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('new_comment.html', comment_form= form, blog_id=blog_id)

@main.route('/delete_comment/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def delete_comment(comment_id):
    comment =Comment.query.get(comment_id)
    if comment.user.id != current_user.id:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('main.index'))

    
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
    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    