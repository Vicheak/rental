// Copyright (c) 2025, dev@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {
        
	},
    get_summary(frm) {
        frm.get_field("summary").$wrapper.append("<h1>Here is your summary</h1>");
    }
});

//current form with client script
//cur_frm.get_field("summary").$wrapper.append("<h1>Hello</h1>")
