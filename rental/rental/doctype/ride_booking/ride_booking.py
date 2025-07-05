# Copyright (c) 2025, dev@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	
	# run before everthing, even saving
	def validate(self):
		if not self.rate:
			# frappe.throw("Please provide a rate")
			self.rate = frappe.db.get_single_value("Rentals Settings", "standard_rate")

		total_distance = 0
		for item in self.items:
			total_distance += item.distance
		
		self.total_amount = total_distance * self.rate


# Python script
# ride = frappe.get_doc("Ride Booking", "bdbgetkv9k")
# ride.vehicle
# ride.order
# ride.items
# for item in ride.items:
# 	print(item.source, item.destination, item.distance)

# frappe.db.get_single_value("Rentals Settings", "standard_rate")
# frappe.db.get_singles_dict("Rentals Settings")
# frappe.get_single("Rentals Settings")
# frappe.get_single("Rentals Settings").standard_rate
