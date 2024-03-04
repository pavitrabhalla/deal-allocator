from decimal import Decimal
import json


def read_json_file(filename):
	with open(filename, 'r') as file:
		data = json.load(file)
	return data


def div_by_zero(a, b):
	return a / b if b != 0 else 0


def parse_deal_inputs(inputs):
	try:
		allocation = Decimal(inputs['allocation_amount'])
		investor_amounts = inputs['investor_amounts']
		for i_a in investor_amounts:
			i_a['requested_amount'] = Decimal(i_a['requested_amount'])
			i_a['average_amount'] = Decimal(i_a['average_amount'])
	except Exception as e:
		raise e
	return allocation, investor_amounts
