from flask import Flask
from config import Configuration


def create_app(config_class=Configuration):
    app = Flask(__name__)
    app.config.from_object(Configuration)

    from czech_app.lesson_1.lesson_1 import lesson1
    app.register_blueprint(lesson1)

    return app
