from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Articles Website Online'
    sport_news = get_news("sports")
    general_news = get_news('general')
    health_news = get_news('health')
    return render_template('index.html', title = title,sports=sport_news,general=general_news,health=health_news)
    

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)