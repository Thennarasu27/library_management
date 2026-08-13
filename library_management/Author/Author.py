import frappe


def get_context(context):
    author_name = frappe.form_dict.name

    author_doc_name = frappe.db.get_value(
        "Author",
        {"author1": author_name},
        "name"
    )

    if not author_doc_name:
        frappe.throw("Author not found")

    author = frappe.get_doc(
        "Author",
        author_doc_name
    )

    context.author = author