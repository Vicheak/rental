// Copyright (c) 2025, dev@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {
        console.log("Running load...")
    },
    setup(frm) {
        console.log("Setting up...")  
    },
	refresh(frm) {
        console.log("On refresh...")

        // if(frm.doc.status === "New") {
        //     frm.add_custom_button("Accept", () => {
        //         // frappe.show_alert("Hello Ride Order")
        //         //status => Accepted
        //         frm.set_value("status", "Accepted")
        //         //save the form
        //         frm.save()
        //     })

        //     frm.add_custom_button("Reject", () => {
        //         //status => Rejected
        //         frm.set_value("status", "Rejected")
        //         //save the form
        //         frm.save()
        //     })
        // }

        //grouping buttons
        if(frm.doc.status === "New") {
            frm.add_custom_button("Accept", () => {
                // frappe.show_alert("Hello Ride Order")
                //status => Accepted
                frm.set_value("status", "Accepted")
                //save the form
                frm.save()
            }, "Actions")

            frm.add_custom_button("Reject", () => {
                //status => Rejected
                frm.set_value("status", "Rejected")
                //save the form
                frm.save()
            }, "Actions")
        }
	},
    status(frm) {
        console.log("Status changed!")
    }
});
