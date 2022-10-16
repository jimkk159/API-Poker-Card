import uuid
import random
from flask import request, Blueprint, jsonify

suits = ["spade", "heart", "diamond", "club"]
poker_symbol = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
poker_value_dict = {"K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5,
                    "4": 4, "3": 3, "2": 2, "A": 1}

card_blueprint = Blueprint('card', __name__)


def get_specific_card(symbol="A", suit="spade", faced=False):
    card = {
        "id": uuid.uuid1(),
        "symbol": symbol,
        "suit": suit,
        "faced": faced
    }
    return card


@card_blueprint.route("/random_card")
def get_random_card():
    faced = False
    if "faced" in request.args:
        faced = True
    return jsonify(get_specific_card(symbol=random.choice(poker_symbol), suit=random.choice(suits), faced=faced))


@card_blueprint.route("/card")
def get_card():
    faced = False
    if "faced" in request.args:
        faced = True
    if "symbol" not in request.args:
        return 404
    if "suit" not in request.args:
        return 404
    symbol = request.args["symbol"]
    suit = request.args["suit"]

    return jsonify(get_specific_card(symbol=symbol, suit=suit, faced=faced))



