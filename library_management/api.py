import frappe


@frappe.whitelist()
def task_subject(sub):
    doc = frappe.new_doc('task_assign')
    doc.subject=sub
    doc.save()
    
@frappe.whitelist()
def get():
    return frappe.db.get_list("Employee Management")
# list user permission but all not applies.
@frappe.whitelist()
def get_all():
    return frappe.db.get_all("Employee Management")

@frappe.whitelist()
def get_value():
    return frappe.db.get_value(
        "Employee Management",
        "2",
        "name1"
    )

@frappe.whitelist()
def get_single_value():
    return frappe.db.get_single_value(
        "single",
        "name1"
    )

@frappe.whitelist()
def set_value():
    result= frappe.db.set_value(
        "Employee Management",
        "10",
        "name1",
        "NarenMS"
    )
    commit()
    return "done"

@frappe.whitelist() # not working properly
def exists():
    res=frappe.db.exists(
        "Employee Management",
        {"name1":"NarenMS"}
    )
    return res

@frappe.whitelist()
def count():
    return frappe.db.count(
        "Employee Management"
    )

@frappe.whitelist()
def delete():
    res=frappe.db.delete(
        "Employee Management",
        {
            "name": "13"
        }
    )
    commit()
    return res

# @frappe.whitelist()
# def truncate_employees():
#     return frappe.db.truncate(
#         "Employee Management"
#     )

@frappe.whitelist()
def commit():
    return frappe.db.commit()

# @frappe.whitelist()
# def savepoint():
#     return frappe.db.savepoint("employee_savepoint")

# @frappe.whitelist()
# def rollback():
#     return frappe.db.rollback()

@frappe.whitelist()
def test():
    before = frappe.db.get_value("Employee Management","10","name1")
    frappe.db.set_value(
        "Employee Management",
        "10",
        "name1",
        "Naren MS"
    )
    frappe.db.savepoint("a")
    frappe.db.set_value(
        "Employee Management",
        "2",
        "name1",
        "DEEPAK R"
    )
    #frappe.db.rollback(save_point="a");
    commit();
    after = frappe.db.get_value("Employee Management","2","name1")
    return after

@frappe.whitelist()
def sql():
    return frappe.db.sql(
        """
        SELECT name
        FROM `tabEmployee Management`
        """
    )

@frappe.whitelist()
def multisql():
    return frappe.db.multisql({
        "mariadb": """
            SELECT name
            FROM `tabEmployee Management`
        """,
        "postgres": """
            SELECT name
            FROM "tabEmployee Management"
        """
    })

# @frappe.whitelist()
# def rename_table():
#     return frappe.db.rename_table(
#         "tabEmployee Management",
#         "Employee Management"
#     )


@frappe.whitelist()
def describe():
    return frappe.db.describe(
        "Employee Management"
    )

# @frappe.whitelist()
# def change_column_type():
#     return frappe.db.change_column_type(
#         "Employee Management",
#         "employee_name",
#         "VARCHAR(255)"
#     )

@frappe.whitelist()
def add():
    return frappe.db.sql("""
    SHOW INDEX FROM `tabEmployee Management`
            """, as_dict=True)
            
@frappe.whitelist()
def add_index():
    frappe.db.add_index(
        "Employee Management",
        ["name1"],
        "idx"
    )
    add()

# @frappe.whitelist() ##not working
# def add_unique():
#     frappe.db.add_unique(
#         "Employee Management",
#         ["email"],
#         "emailidx"
#     )
#     return "unique-added"

@frappe.whitelist()
def bulk_update():
    res=frappe.db.bulk_update(
        "Employee Management",
        {
            "11": {
                "name1": "11-changed",
            },
            "7": {
                "name1": "7-changed",
            }
        }
    )
    commit()
    return "changed"

