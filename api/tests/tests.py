from api.modules.utils import parse_deal_inputs
from api.modules.utils import read_json_file
from api.modules.prorater import Prorater
import unittest


class TestProrate(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestProrate, self).__init__(*args, **kwargs)
		self.prorater = Prorater()

	def test_complex_1(self):
		test_input = read_json_file('api/tests/test_data/complex_1_input.json')
		allocation, investor_amounts = parse_deal_inputs(test_input)
		self.assertEqual(self.prorater.prorate(allocation, investor_amounts), read_json_file(
			'api/tests/test_data/complex_1_output.json'))

	def test_complex_2(self):
		test_input = read_json_file('api/tests/test_data/complex_2_input.json')
		allocation, investor_amounts = parse_deal_inputs(test_input)
		self.assertEqual(self.prorater.prorate(allocation, investor_amounts), read_json_file(
			'api/tests/test_data/complex_2_output.json'))

	def test_simple_1(self):
		test_input = read_json_file('api/tests/test_data/simple_1_input.json')
		allocation, investor_amounts = parse_deal_inputs(test_input)
		self.assertEqual(self.prorater.prorate(allocation, investor_amounts), read_json_file(
			'api/tests/test_data/simple_1_output.json'))

	def test_simple_2(self):
		test_input = read_json_file('api/tests/test_data/simple_2_input.json')
		allocation, investor_amounts = parse_deal_inputs(test_input)
		self.assertEqual(self.prorater.prorate(allocation, investor_amounts), read_json_file(
			'api/tests/test_data/simple_2_output.json'))

	def test_single_investor(self):
		test_input = read_json_file('api/tests/test_data/single_investor_input.json')
		allocation, investor_amounts = parse_deal_inputs(test_input)
		self.assertEqual(self.prorater.prorate(allocation, investor_amounts), read_json_file(
			'api/tests/test_data/single_investor_output.json'))

	def test_large_request_low_average(self):
		test_input = read_json_file('api/tests/test_data/large_request_low_average_input.json')
		allocation, investor_amounts = parse_deal_inputs(test_input)
		self.assertEqual(self.prorater.prorate(allocation, investor_amounts), read_json_file(
			'api/tests/test_data/large_request_low_average_output.json'))

	def test_negative_request(self):
		test_input = read_json_file('api/tests/test_data/negative_request_input.json')
		allocation, investor_amounts = parse_deal_inputs(test_input)
		self.assertEqual(self.prorater.prorate(allocation, investor_amounts), read_json_file(
			'api/tests/test_data/negative_request_output.json'))


if __name__ == '__main__':
	unittest.main()
