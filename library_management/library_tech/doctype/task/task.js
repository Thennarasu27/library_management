// Copyright (c) 2026, Thennarasu M and contributors
// For license information, please see license.txt
// frappe.ui.form.on("task", {
// 	refresh(frm) {
// 	},
// });
frappe.ui.form.on("task", {
    refresh(frm) {
        frm.add_custom_button("Open Dialog", function () {

            let d = new frappe.ui.Dialog({
                title: "Create Task",
                fields: [
                    {
                        label: "Task Subject",
                        fieldname: "task_subject",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],
                primary_action_label: "Create Task",
                primary_action(values) {
                    frappe.call({
                        method: "library_management.library_tech.doctype.task.task.create_task",
                        args: {
                            task_subject: values.task_subject
                        },
                        callback: function(r) {
                            d.hide();

                            frappe.msgprint({
                                title: "Success",
                                message:"task created successfully",
                                indicator: "green"
                            });
                        }
                    });
                }
            });
            d.show();
        });
    }
});
