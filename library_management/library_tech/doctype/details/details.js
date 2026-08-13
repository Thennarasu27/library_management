// Copyright (c) 2026, Thennarasu M and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Details", {
// 	refresh(frm) {

// 	},
// // });

//         frappe.ui.form.on("Details", {
//     refresh(frm) {
//         console.log("Refresh");
//     },

//     timeline_refresh(frm) {
//         console.log("Timeline Refresh");
//     }
// });
frappe.ui.form.on("Details", {
    get_email_recipients(frm, field) {
        if (field === "recipients") {
            return ["pooja16.shivk@gmail.com"];
        }
        if (field === "cc") {
            return ["monikarthik2122@gmail.com"];
        }
        return [];
    }
});