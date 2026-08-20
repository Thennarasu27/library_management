import frappe
def before_tests():
    frappe.throw("BEFORE_TESTS WAS CALLED", "before_tests hook")