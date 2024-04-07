from flask import Blueprint, render_template #help us organize our files
import random


views = Blueprint('views', __name__)


@views.route('/')
def home():
    numbers = range(1, 12)
    views= random.randint(1, 1000)
    likes= random.randint(1, 1000)
    comments= random.randint(1, 1000)
    return render_template("home.html",  name='Dexter', numbers=numbers, views=views, likes=likes, comments=comments)

@views.route('/test')
def test():
    return render_template("test.html")


