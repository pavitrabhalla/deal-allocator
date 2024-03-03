from typing import Set, Dict, Union, Any, List

from flask import Flask
from flask import request
from prorater import Prorater
import input_parser as parser
app = Flask(__name__)


# POST endpoint
@app.post('/api/prorate')
def prorate():
    prorater = Prorater()
    try:
        data = request.get_json(force=True)
        allocation, investor_amounts = parser.parsed_inputs(data)
        investments = prorater.prorate(allocation, investor_amounts)
        return __create_deal_response(investments)
    # Very generic error handling for the sake of this example
    except Exception as e:
        return {'error': e.__str__()}, 400


def __create_deal_response(investments: dict) -> dict[str, list[dict[str, Union[float, Any]]]]:
    return {'deal': [{'name': k, 'investment': float(v)} for k, v in investments.items()]}
