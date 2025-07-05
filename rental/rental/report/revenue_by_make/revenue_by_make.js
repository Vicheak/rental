// Copyright (c) 2025, dev@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by Make"] = {
	filters: [
		// {
		// 	"fieldname": "my_filter",
		// 	"label": __("My Filter"),
		// 	"fieldtype": "Data",
		// 	"reqd": 1,
		// },
		{
			"fieldname": "my_filter",
			"label": "My Filter",
			"fieldtype": "Link",
			"options": "Vehicle"
		}
	],
};
