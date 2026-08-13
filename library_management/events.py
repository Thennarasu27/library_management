import frappe
def before_save(doc, method):
    frappe.msgprint("Before Save Hook Called")
def after_insert(doc, method):
    frappe.msgprint("After Insert Hook Called")