import frappe
def before_install():
    frappe.msgprint("Library Management: before_install executed")
def after_install():
    frappe.msgprint("Library Management: after_install executed")
def after_sync():
    frappe.msgprint("Library Management: after_sync executed")