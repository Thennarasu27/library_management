import frappe

def before_uninstall():
    frappe.msgprint("Library Management: before_uninstall executed")
def after_uninstall():
    frappe.msgprint("Library Management: after_uninstall executed")