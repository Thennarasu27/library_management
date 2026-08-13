frappe.pages['practice'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'None',
		single_column: true
	});
	page.set_title("Employee Dashboard");
	page.set_title_sub("Total Employees: 25");
	page.set_indicator("Active", "blue");
	page.set_primary_action("New Employee", () => {
     frappe.msgprint("Clicked");
});
page.set_secondary_action("Refresh", () => {
    frappe.msgprint("Refreshing");
});
page.clear_primary_action()
page.clear_secondary_action()

// page.add_menu_item("Export", () => {
//     frappe.msgprint("Export");
// });
//page.clear_menu()
// page.add_action_item("Delete", () => {
//     frappe.msgprint("Deleted");
// });
// page.add_action_item("Deleted2", () => {
//     frappe.msgprint("Deleted");
// });
page.add_inner_button("Update", () => {
    frappe.msgprint("Updated");
});
//page.remove_inner_button("Update");
page.add_inner_button("PDF", () => {}, "Export");
page.add_inner_button("Excel", () => {}, "Export");
page.change_inner_button_type(
    "Update",
    null,
    "danger"
);
//page.clear_inner_toolbar();
let field = page.add_field({
    label: "Department",
    fieldtype: "Select",
    fieldname: "department",
    options: [
        "IT",
        "HR",
        "Sales"
    ],
	change() {
        console.log(page.get_form_values());
    }
    
});
page.clear_fields();
let val = page.get_form_values();
console.log(val);}
