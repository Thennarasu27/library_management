// Copyright (c) 2026, Thennarasu M and contributors
// For license information, please see license.txt

frappe.ui.form.on("task_assign", {
    refresh(frm) {

        let dia = new frappe.ui.Dialog({
            title: "Enter Subject",

            fields: [
                {
                    label: "Subject",
                    fieldname: "subject",
                    fieldtype: "Data",
                }
            ],

            primary_action_label: "Submit",

            primary_action(values) {

                frappe.call({
                    method: "library_management.api.task_subject",

                    args: {
                        sub: values.subject
                    },

                    callback: function(r) {

                        dia.hide();

                        frappe.msgprint({
                            title: "Success",
                            message: "Task " + r.message + " created successfully.",
                            indicator: "green"
                        });

                    }
                });
            }
        });

        dia.show();
    }
});