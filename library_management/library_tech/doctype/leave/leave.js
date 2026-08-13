// Copyright (c) 2026, Thennarasu M and contributors
// For license information, please see license.txt

frappe.ui.form.on("Leave", {
	setup(frm) {
        frm.set_query("name1",function(){
            return{
                filters:{
                    name1:"Thennarasu"
                }
            }
        })
	},
});
