// Copyright (c) 2025, dev@gmail.com and contributors
// For license information, please see license.txt

//on Ride Booking doctype
frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        // frm.add_custom_button("Accept", () => {
        //     frappe.show_alert("Hello Ride Booking")
        // })
	},
    
    rate(frm) {
        //recalculate total
        frm.trigger("update_total_amount");
    },

    update_total_amount(frm) {
        let total_d = 0;
        for(let item of frm.doc.items){
            // console.log(item.distance)
            total_d += item.distance;
        }

        const amount = total_d * frm.doc.rate;
        frm.set_value("total_amount", amount)
    }
});

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
        
	},

    distance(frm, cdt, cdn) {
        //cdt = child table doctype, cdn = child table doc name
        // console.log(cdt, cdn);
        // console.log("Child table distance changed!");
        
        //get from client side form not from database
        // console.log(frappe.get_doc(cdt, cdn));

        // my_child = frappe.get_doc(cdt, cdn);
        // frappe.model.set_value(cdt, cdn, "source", "Updated source");

        // let total_d = 0;
        // for(let item of frm.doc.items){
        //     // console.log(item.distance)
        //     total_d += item.distance;
        // }

        // const amount = total_d * frm.doc.rate;
        // frm.set_value("total_amount", amount);

        frm.trigger("update_total_amount");
    },

    items_add(frm) {
        frm.trigger("update_total_amount");
    },

    items_remove(frm) {
        frm.trigger("update_total_amount");
    }
})


//current form with JS object
//cur_fm
//cur_frm.doc.rate
//cur_frm.set_intro("Hello myapp", "red")
//cur_frm.set_value("rate", 60)
//cur_frm.save()
//cur_frm.add_custom_button("Accept", () => {console.log("button click!")})
