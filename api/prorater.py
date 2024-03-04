from decimal import Decimal
from decimal import getcontext
from utils import div_by_zero


class Prorater:
	def __init__(self):
		getcontext().prec = 7

	# Public method used to allocate funds to investors
	@staticmethod
	def prorate(allocation: Decimal, investor_amounts: list) -> dict:
		investors_sanitized = Prorater.__sanitize_and_prep_investor_amounts(investor_amounts)
		prorate_enabled = Prorater.__should_prorate(allocation, investors_sanitized)
		if prorate_enabled:
			investments = Prorater.__do_prorated_allocation(
				allocation, allocation, investors_sanitized, {}, investors_sanitized)
		else:
			investments = Prorater.__allocate_requested(investors_sanitized)

		return Prorater.__to_float(investments)

	# Handle negative values for requested amount or averages. Ignore investors	with negative values
	@staticmethod
	def __sanitize_and_prep_investor_amounts(investor_amounts: list) -> list:
		investor_amounts = [
			i for i in investor_amounts if i.get('average_amount', 0) > 0 and i.get('requested_amount', 0) > 0
		]

		for i_a in investor_amounts:
			i_a['average_multiplier'] = div_by_zero(i_a['average_amount'], sum(i_a['average_amount'] for i_a in investor_amounts))

		return investor_amounts

	# Terminate allocation if the remaining allocation is tending to zero or there are no remaining investors
	@staticmethod
	def __terminate_allocation(allocation: Decimal, remaining_investors: list) -> bool:
		if allocation <= Decimal(pow(2, -149)) or not remaining_investors:
			return True
		return False

	# Used to allocate funds using proration when the total allocation is less than the total requested amount
	# Calls itself recursively until the total allocation remaining is tending to zero
	@staticmethod
	def __do_prorated_allocation(total_allocation: Decimal, remaining_allocation: Decimal,
			remaining_investors, investments: dict, investor_amounts: list) -> dict:
		if Prorater.__terminate_allocation(remaining_allocation, remaining_investors):
			return investments

		remaining_allocation, remaining_investors, investments, investor_amounts = (
			Prorater.__allocate_prorated(remaining_allocation, remaining_investors, investments, investor_amounts)
		)
		return Prorater.__do_prorated_allocation(
			total_allocation, remaining_allocation, remaining_investors, investments, investor_amounts)

	@staticmethod
	def __to_float(investments: dict) -> dict:
		return {k: float(v) for k, v in investments.items()}

	# For the last investor, allocate the remaining amount appropriately
	@staticmethod
	def __handle_last_investor(remaining: Decimal, investor: dict, investments: dict, investor_amounts: list):
		i_name = investor['name']
		i_allocation = investor['requested_amount'] \
			if i_name in investments and investor['requested_amount'] < remaining else remaining
		remaining -= i_allocation

		investments[i_name] = investments[i_name] + i_allocation if i_name in investments else i_allocation
		remaining_investors = []
		return remaining, remaining_investors, investments, investor_amounts

	# Implements rules for calculating prorated allocation
	@staticmethod
	def __allocate_prorated(allocation: Decimal, remaining_investors: list, investments: dict, investor_amounts: list):
		remaining = allocation

		if len(remaining_investors) == 1:
			return Prorater.__handle_last_investor(remaining, remaining_investors[0], investments, investor_amounts)

		for i_a in investor_amounts:
			# Skip investors that have already been allocated their requested amount
			if i_a['requested_amount'] <= 0:
				continue

			i_allocation = allocation * i_a['average_multiplier']

			# If the investor can get their remaining requested amount, allocate it
			if i_allocation > i_a['requested_amount']:
				i_allocation = i_a['requested_amount']

			remaining -= i_allocation
			investments[i_a['name']] = investments[i_a['name']] + i_allocation if \
				(i_a['name'] in investments) else i_allocation
			i_a['requested_amount'] -= i_allocation

		# Remove investors that have been allocated their requested amount
		remaining_investors = [
			investor for investor in investor_amounts if
			investor['requested_amount'] > 0
		]

		return remaining, remaining_investors, investments, investor_amounts

	# Used to allocate funds when the total allocation is greater than the total requested amount
	@staticmethod
	def __allocate_requested(investor_amounts: list):
		investments = {}
		for i_a in investor_amounts:
			investments[i_a['name']] = i_a['requested_amount']
		return investments

	# Used to determine if proration is necessary
	@staticmethod
	def __should_prorate(allocation: Decimal, investor_amounts: list):
		total_requested_amount = sum(i_a['requested_amount'] for i_a in investor_amounts)
		return total_requested_amount > allocation

