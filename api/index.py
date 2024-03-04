from flask import Flask
from flask import request
from api.prorater import Prorater
from utils import parse_deal_inputs

app = Flask(__name__)


# POST endpoint
@app.post('/api/prorate')
def prorate():
    try:
        data = request.get_json(force=True)
        allocation, investor_amounts = parse_deal_inputs(data)
        investments = Prorater.prorate(allocation, investor_amounts)
        return __create_deal_response(investments)
    # Very generic error handling for the sake of this example
    except Exception as e:
        return {'error': e.__str__()}, 400


def __create_deal_response(investments: dict) -> dict[str, list]:
    return {'deal': [{'name': k, 'investment': float(v)} for k, v in investments.items()]}
