from .request import 

# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     popular_movies = get_movies('popular')
#     print(popular_movies)
#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title,popular = popular_movies)

@app.route('/opinion', methods = ['GET','POST'])
def new_opinion():
    form = OpinionForm()

    if form.validate_on_submit():
        title = form.title.data
        opinion = form.opinion.data
        new_opinion = Opinion(text)
        new_opinion.save_opinion()
        return redirect(url_for('index'))

    title = 'Opinion'
    return render_template('opinion.html',title = title, opinion_form=form)
