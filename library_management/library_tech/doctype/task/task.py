# Copyright (c) 2026, Thennarasu M and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
#@frappe.whitelist()
#def function():
class task(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.
	from typing import TYPE_CHECKING
	if TYPE_CHECKING:
		from frappe.types import DF
		task_subject: DF.Data | None
	# end: auto-generated types
	pass
@frappe.whitelist()
def create_task(task_subject):
	task=frappe.new_doc("task")
	task.task_subject=task_subject
	task.save()
	return task.name
