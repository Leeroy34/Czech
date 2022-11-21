from flask import render_template, Blueprint, request


lesson1 = Blueprint('lesson_1', __name__)


@lesson1.route('/')
def first_lesson():
    return render_template('base.html')
