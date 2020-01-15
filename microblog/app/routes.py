from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sidd'}
    posts = [
        {
            'author': {'username': 'Muteeb'},
            'body': 'Beautiful day in New York!'
        },
        {
            'author': {'username': 'Ben'},
            'body': 'The COD game is so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)