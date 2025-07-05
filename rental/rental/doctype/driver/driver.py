# Copyright (c) 2025, dev@gmail.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

# this is the Driver controller
class Driver(Document):

	# def autoname(self):
	# 	if self.age > 0

	# this is the controller hook
	def before_save(self):
		print("================= Running the hook before_save Driver")
		self.full_name = f"{self.first_name} {self.last_name}"

	def send_alert(self):
		print("Sending message")
		

# example of Python ORM
# frappe.db.get_value("Driver", "DR-001", "first_name")
# frappe.get_doc("Driver", "DR-001")
# frappe.new_doc("Driver")
# d = frappe.new_doc("Driver")
# d.first_name = "mi"
# d.last_name = "joli"
# d.license_number = "LIC1234"
# d.save()
# frappe.db.commit()
# d.send_alert()
# drivers = frappe.get_all("Driver")


# API Secret : 7725ad7bf815dbc
