"""
	customer.py

	Initializes and stores information about each customer (namely, their phone number, as well as an automated ID counter primary key)
"""

from app import db

class Customer(db.Model):

	# initialize table name
	__tablename__ = "customers"

	# set columns of db
	id = db.Column(db.Integer, primary_key=True)
	phone = db.Column(db.String())

	# init
	def __init__(self, phone):
		self.phone = phone

	# print 
	def __repr__(self):
		return f"ID = {self.id}, Phone = {self.phone}"

	# serialize
	def serialize(self):
		return {
			'id':self.id, 
			'phone':self.phone
		}
