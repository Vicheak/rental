# Copyright (c) 2025, dev@gmail.com and contributors
# For license information, please see license.txt

import frappe
# from frappe import _


# def execute(filters: dict | None = None):
# 	"""Return columns and data for the report.

# 	This is the main entry point for the report. It accepts the filters as a
# 	dictionary and should return columns and data. It is called by the framework
# 	every time the report is refreshed or a filter is updated.
# 	"""
# 	columns = get_columns()
# 	data = get_data()

# 	return columns, data


# def get_columns() -> list[dict]:
# 	"""Return columns for the report.

# 	One field definition per column, just like a DocType field definition.
# 	"""
# 	return [
# 		{
# 			"label": _("Column 1"),
# 			"fieldname": "column_1",
# 			"fieldtype": "Data",
# 		},
# 		{
# 			"label": _("Column 2"),
# 			"fieldname": "column_2",
# 			"fieldtype": "Int",
# 		},
# 	]


# def get_data() -> list[list]:
# 	"""Return data for the report.

# 	The report data is a list of rows, with each row being a list of cell values.
# 	"""
# 	return [
# 		["Row 1", 1],
# 		["Row 2", 2],
# 	]

def execute(filters: dict | None = None):

	# print("--"*20)
	# print(filters)
	# debug on the frontend also
	# frappe.errprint(filters)

	columns = [
		{
			"fieldname": "make",
			"label": "Make",
			"fieldtype": "Data"
		},
		{
			"fieldname": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"options": "USD"
		}
	]
    
	data = frappe.get_all(
        "Ride Booking", 
        fields=["SUM(total_amount) AS total_revenue", "vehicle.make"], 
        filters={"docstatus": 1}, 
        group_by="make"
	)

	chart = {
		"data": {
			"labels": [x.make for x in data],
			"datasets": [{"values": [x.total_revenue for x in data]}],
		},
		"type": "pie"
		# "type": "bar"
		# "type": "line"
		# "type": "donut"
	}

	return columns, data, "Here is the report", chart

# Python ORM
# frappe.get_all("Ride Booking", fields=["total_amount", "vehicle"])
# frappe.get_all("Ride Booking", fields=["total_amount", "vehicle"], filters={"docstatus": ("<", 2)})
# frappe.get_all("Ride Booking", fields=["total_amount", "vehicle"], filters={"docstatus": 1})
# frappe.get_all("Ride Booking", fields=["total_amount", "vehicle.make"], filters={"docstatus": 1})
# frappe.get_all("Ride Booking", fields=["SUM(total_amount)", "vehicle.make"], filters={"docstatus": 1}, group_by="make")
# frappe.get_all("Ride Booking", fields=["SUM(total_amount)", "vehicle.make", "COUNT(*)"], filters={"docstatus": 1}, group_by="make")
# frappe.get_all("Ride Booking", fields=["SUM(total_amount) AS total_revenue", "vehicle.make"], filters={"docstatus": 1}, group_by="make")
