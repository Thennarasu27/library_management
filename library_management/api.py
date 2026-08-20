# import frappe
# import time

# def my_background_job():
#     print("Background job started")
#     time.sleep(10)
#     print("Background job finished")

# @frappe.whitelist()
# def start_job():
#     frappe.enqueue(
#         "library_management.api.my_background_job",
#         queue="short"
#     )
#     return "Job added to queue"

# @frappe.whitelist()
# def task_subject(sub):
#     doc = frappe.new_doc('task_assign')
#     doc.subject=sub
#     doc.save()
    
# @frappe.whitelist()
# def get():
#     return frappe.db.get_list("Employee Management")
# # list user permission but all not applies.
# @frappe.whitelist()
# def get_all():
#     return frappe.db.get_all("Employee Management")

# @frappe.whitelist()
# def get_value():
#     return frappe.db.get_value(
#         "Employee Management",
#         "2",
#         "name1"
#     )

# @frappe.whitelist()
# def get_single_value():
#     return frappe.db.get_single_value(
#         "single",
#         "name1"
#     )

# @frappe.whitelist()
# def set_value():
#     result= frappe.db.set_value(
#         "Employee Management",
#         "10",
#         "name1",
#         "NarenMS"
#     )
#     commit()
#     return "done"

# @frappe.whitelist() # not working properly
# def exists():
#     res=frappe.db.exists(
#         "Employee Management",
#         {"name1":"NarenMS"}
#     )
#     return res

# @frappe.whitelist()
# def count():
#     return frappe.db.count(
#         "Employee Management"
#     )

# @frappe.whitelist()
# def delete():
#     res=frappe.db.delete(
#         "Employee Management",
#         {
#             "name": "13"
#         }
#     )
#     commit()
#     return res

# # @frappe.whitelist()
# # def truncate_employees():
# #     return frappe.db.truncate(
# #         "Employee Management"
# #     )

# @frappe.whitelist()
# def commit():
#     return frappe.db.commit()

# # @frappe.whitelist()
# # def savepoint():
# #     return frappe.db.savepoint("employee_savepoint")

# # @frappe.whitelist()
# # def rollback():
# #     return frappe.db.rollback()

# @frappe.whitelist()
# def test():
#     before = frappe.db.get_value("Employee Management","10","name1")
#     frappe.db.set_value(
#         "Employee Management",
#         "10",
#         "name1",
#         "Naren MS"
#     )
#     frappe.db.savepoint("a")
#     frappe.db.set_value(
#         "Employee Management",
#         "2",
#         "name1",
#         "DEEPAK R"
#     )
#     #frappe.db.rollback(save_point="a");
#     commit();
#     after = frappe.db.get_value("Employee Management","2","name1")
#     return after

# @frappe.whitelist()
# def sql():
#     return frappe.db.sql(
#         """
#         SELECT name
#         FROM `tabEmployee Management`
#         """
#     )

# @frappe.whitelist()
# def multisql():
#     return frappe.db.multisql({
#         "mariadb": """
#             SELECT name
#             FROM `tabEmployee Management`
#         """,
#         "postgres": """
#             SELECT name
#             FROM "tabEmployee Management"
#         """
#     })

# # @frappe.whitelist()
# # def rename_table():
# #     return frappe.db.rename_table(
# #         "tabEmployee Management",
# #         "Employee Management"
# #     )


# @frappe.whitelist()
# def describe():
#     return frappe.db.describe(
#         "Employee Management"
#     )

# # @frappe.whitelist()
# # def change_column_type():
# #     return frappe.db.change_column_type(
# #         "Employee Management",
# #         "employee_name",
# #         "VARCHAR(255)"
# #     )

# @frappe.whitelist()
# def add():
#     return frappe.db.sql("""
#     SHOW INDEX FROM `tabEmployee Management`
#             """, as_dict=True)
            
# @frappe.whitelist()
# def add_index():
#     frappe.db.add_index(
#         "Employee Management",
#         ["name1"],
#         "idx"
#     )
#     add()

# # @frappe.whitelist() ##not working
# # def add_unique():
# #     frappe.db.add_unique(
# #         "Employee Management",
# #         ["email"],
# #         "emailidx"
# #     )
# #     return "unique-added"

# @frappe.whitelist()
# def bulk_update():
#     res=frappe.db.bulk_update(
#         "Employee Management",
#         {
#             "11": {
#                 "name1": "11-changed",
#             },
#             "7": {
#                 "name1": "7-changed",
#             }
#         }
#     )
#     commit()
#     return "changed"

#server calls ajax 

# import frappe

# @frappe.whitelist()
# def func1():
#     return "Hello from server!"

# @frappe.whitelist()
# def func2(name):
#     return f"Hello {name}!"

# @frappe.whitelist()
# def func3():
#     doc = frappe.db.get_doc(
#         "Employee Management",
#         "7"
#     )
#     return doc

# @frappe.whitelist()
# def func4():
#     records = frappe.db.get_list(
#         "Employee Management",
#         fields=["name", "name1"]
#     )
#     return records

# @frappe.whitelist()
# def func5():
#     value = frappe.db.get_value(
#         "Employee Management",
#         "7",
#         "name1"
#     )
#     return value

# @frappe.whitelist()
# def func6():
#     value = frappe.db.get_single_value(
#         "single",
#         "name1"
#     )
#     return value

# @frappe.whitelist()
# def func7():
#     result = frappe.db.set_value(
#         "Employee Management",
#         "7",
#         "name1",
#         "Updated Name"
#     )
#     return "done"

# @frappe.whitelist()
# def func8():
#     doc = frappe.get_doc({
#         "doctype": "Employee Management",
#         "name1": "New Employee"
#     })
#     doc.insert()
#     return doc

# @frappe.whitelist()  #not working
# def func9():
#     count = frappe.db.count(
#         "Employee Management"
#     )
#     return count

# @frappe.whitelist()
# def func10():
#     frappe.delete_doc(
#         "Employee Management",
#         "15"
#     )
#     return "Document 15 deleted successfully"

# @frappe.whitelist()
# def func11():
#     exists = frappe.db.exists(
#         "Employee Management",
#         "7"
#     )
#     if exists:
#         return "yes"


# query builder


# import frappe
# from frappe.query_builder.functions import Count

# @frappe.whitelist()
# def func1():
#     res = frappe.qb.from_("Employee Management").select("name1")
#     return res.run()
# @frappe.whitelist()
# def func2():
#     Employee = frappe.qb.DocType("Employee Management")
#     res = (
#         frappe.qb.from_(Employee)
#         .select(Employee.name1)
#     )
#     return res.run()
# @frappe.whitelist()
# def func3():
#     Employee = frappe.qb.DocType("Employee Management")
#     res = (
#         frappe.qb.from_(Employee)
#         .select(Employee.name1)
#         .where(Employee.name1=="Thennarasu M")
#     )
#     return str(res)

# @frappe.whitelist()
# def func4():
#     Employee = frappe.qb.DocType("Employee Management")
#     res = (
#         frappe.qb.from_(Employee)
#         .select(Employee.name1)
#     )
#     return res.get_sql()
# # for where and .where().where() then for or .where()|.where()

# @frappe.whitelist()
# def func5():
#     Employee = frappe.qb.DocType("Employee Management")
#     res = (
#         frappe.qb.from_(Employee)
#         .select(Employee.name1)
#         .where(Employee.name1 == "Thennarasu M")
#     )
#     return res.run(as_dict=True)

# @frappe.whitelist()
# def func6():
#     Employee = frappe.qb.DocType("Employee Management")
#     res = (
#         frappe.qb.from_(Employee)
#         .select(Employee.name1)
#         .where(Employee.name1 == "Thennarasu M")
#     )
#     return frappe.db.sql(res, as_dict=True)

# @frappe.whitelist()
# def func8():
#     Employee = frappe.qb.DocType("Employee Management")
#     count = Count(Employee.name1).as_("total_employees")
#     res = (
#         frappe.qb.from_(Employee)
#         .select(count)
#     )
#     return res.run()

# @frappe.whitelist()
# def func9():
#     Employee = frappe.qb.DocType("Employee Management")
#     Leave = frappe.qb.DocType("Leave")
#     query = (
#         frappe.qb.from_(Employee)
#         .inner_join(Leave)
#         .on(Employee.name1 == Leave.name1)
#         .select(
#             Employee.name1,
#             Leave.name1
#         )
#     )

#     return query.run(as_dict=True)


#utility functions

import frappe
from frappe.utils import *

@frappe.whitelist()
def apicheck():
    return "Api call method worked"

@frappe.whitelist()
def func1():
    return now()

@frappe.whitelist()
def func2():
    return getdate()

@frappe.whitelist()
def func3():
    return today()

@frappe.whitelist()
def func4():
    return add_to_date(today(), days=10, as_string=True)

@frappe.whitelist()
def func5():
    date_1 = today()
    date_2 = add_to_date(date_1, days=10)
    return date_diff(date_2, date_1)

@frappe.whitelist()
def func6():
    date_1 = today()
    date_2 = add_to_date(date_1, days=10)
    return days_diff(date_2, date_1)

@frappe.whitelist()
def func7():
    date_1 = "2024-07-01"
    date_2 = add_to_date(date_1, days=60)
    return month_diff(date_2, date_1)

@frappe.whitelist()
def func8():
    return pretty_date(now())

@frappe.whitelist()
def func9():
    return format_duration(10000)

@frappe.whitelist()
def func10():
    return comma_and(
        ["Apple", "Ball", "Cat"],
    )

@frappe.whitelist()
def func11():
    return comma_or(
        ["Apple", "Ball", "Cat"],
    )

@frappe.whitelist()
def func12():
    return money_in_words(900.50)

@frappe.whitelist()
def func13():
    validate_json_string(
        '[{"player": "one", "score": 199}]'
    )
    return "Valid JSON"

@frappe.whitelist()
def func14():
    return random_string(10)

@frappe.whitelist() #not working
def func15():
    return mask_string("1234567890")

@frappe.whitelist()
def func16():
    return unique(
        [1, 2, 3, 1, 1, 4, 3]
    )

@frappe.whitelist()
def func17():
    return get_abbr(
        "Tridots Tech",
        max_len=3
    )

@frappe.whitelist()
def func18():
    return validate_url(
        "https://google.com"
    )



@frappe.whitelist()
def func19():
    return validate_email_address(
        "abcdef, test@example.com, another@example.com"
    )

@frappe.whitelist()
def func20():
    return validate_phone_number(
        "+91-9876543210"
    )

@frappe.whitelist()
def func21():
    return get_filtered_list_url(
        "Employee Management",
        [
            "7"
        ]
    )


@frappe.whitelist()
def func22():
    return get_filtered_list_link(
        "Employee Management",
        [
            "7"
        ],
        "View Employees"
    )



# @frappe.whitelist()
# def func23():
#    


# # func24 - cache
# @frappe.whitelist()
# def func24():



@frappe.whitelist()
def func25():
    frappe.sendmail(
        recipients=["thennarasum27@gmail.com"],
        subject="Test Email",
        message="Hello from Frappe"
    )

    return "Email sent"


# @frappe.whitelist()
# def func26():
#     from frappe.utils.synchronization import filelock

#     with filelock("my_config_lock"):
#         return "File lock acquired"

# @frappe.whitelist()
# def func27():
#     employees = frappe.get_all(
#         "Employee Management",
#         pluck="name"
#     )

#     return get_filtered_list_url(
#         "Employee Management",
#         employees
#     )

# @frappe.whitelist()
# def func28():
#     employees = frappe.get_all(
#         "Employee Management",
#         pluck="name"
#     )

#     return get_filtered_list_link(
#         "Employee Management",
#         employees,
#         "View Employees"
#     )


import frappe


@frappe.whitelist()
def assignment():
    employees = frappe.get_list(
        "Employee Management",
        fields=[
            "name",
            "name1",
            "email",
            "owner"
        ],
        order_by="creation desc",
        limit_page_length=5
    )
    records = []
    for employee in employees:
        owner_email = frappe.db.get_value(
            "User",
            employee.owner,
            "email"
        )
        records.append({
            "name": employee.name,
            "name1": employee.name1,
            "email": employee.email,
            "owner": employee.owner,
            "owner_email": owner_email
        })
    return {
        "timestamp": frappe.utils.now(),
        "records": records
    }