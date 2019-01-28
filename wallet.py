# wallet.py

class InsufficientAmount(Exception):
	pass

class Wallet(object):

	def __init__(self, initial_amount=0):
		self.balance = initial_amount

	def spend_cash(self, amount):		#money we want to spend
		if self.balance < amount:
			raise InsufficientAmount('not enough available to spend {}'.format(amount))
		self.balance -= amount
	
	def add_cash(self, amount):
		self.balance += amount
