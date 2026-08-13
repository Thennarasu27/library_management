// frappe.listview_settings['Employee Management'] = {
// hide_name_column: true,
// hide_name_filter: true,
// // add_fields: ["salary"],
// //     get_indicator(doc) {
// //         if (doc.salary >= 10000) {
// //             return ["High Salary", "green", "salary,>=,10000"];
// //         } else {
// //             return ["Low Salary", "red", "salary,<,10000"];
// //         }},
//     // onload(listview) {
//     //     frappe.msgprint("List view worked");
//     //     listview.filter_area.add([
//     //         ["Employee Management", "id", "=", "13"]
//     //     ])
        
//     //  }
//     // get_form_link(doc) {
//     //     if (doc.id == '10') {
//     //         return ["Employee Management", '2'];
//     //     }

//     //     return ["Employee Management", doc.name];
//     },
//     // before_render()
//     // {
//     //     frappe.msgprint("Before Render");
//     // },
//     // primary_action()
//     // {
//     //     frappe.msgprint("Primary saved")
//     // }
// button: {
//     show(doc) {
//         return true;
//     },
//     get_label() {
//         return "Bonus";
//     },
//     get_description(doc) {
//         return `Give bonus to`;
//     },
//     action(doc) {
//         frappe.msgprint(`Bonus given to`);
//     }
// },
// formatters: {
//      salary(value) {
//         return "₹ " + value;
//     }
//     }
//  };
