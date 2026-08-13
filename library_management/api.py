import frappe

@frappe.whitelist()
def get_student():
    doc = frappe.get_doc("EmployeeManagement", "1")

    print(doc)
    print(type(doc))
    print(doc.student_name)

    return doc.as_dict() 