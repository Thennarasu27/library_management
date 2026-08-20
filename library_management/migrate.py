import frappe
def before_migrate():
    frappe.msgprint("Library Management: before_migrate executed")
def after_migrate():
    frappe.msgprint("Library Management: after_migrate executed")