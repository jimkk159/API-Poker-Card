import random
from flask import Flask, Blueprint, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

# self module
from card import card_blueprint
from deck import deck_blueprint

def create_app():
    app = Flask(__name__)

    # BluePrint
    app.register_blueprint(card_blueprint)
    app.register_blueprint(deck_blueprint)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
