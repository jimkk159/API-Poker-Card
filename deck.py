import random
from flask import request, Blueprint, jsonify
from card import get_specific_card

suits = ["spade", "heart", "diamond", "club"]
poker_symbol = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
poker_value_dict = {"K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5,
                    "4": 4, "3": 3, "2": 2, "A": 1}

deck_blueprint = Blueprint('deck', __name__)


@deck_blueprint.route("/deck")
def get_deck():
    deck = {"deck": [get_specific_card(symbol=symbol, suit=suit) for symbol in poker_symbol for suit in suits]}
    if "shuffle" in request.args:
        random.shuffle(deck["deck"])
    return jsonify(deck)


@deck_blueprint.route("/decks", defaults={"number": 1})
@deck_blueprint.route("/decks/<int:number>")
def get_multi_decks(number):
    deck_num = number
    deck = {"deck": [get_specific_card(symbol=symbol, suit=suit) for symbol in poker_symbol for suit in suits for _ in
                     range(deck_num)]}
    if "shuffle" in request.args:
        random.shuffle(deck["deck"])
    return jsonify(deck)
