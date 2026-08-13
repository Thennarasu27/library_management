# Copyright (c) 2026, Thennarasu M and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Details(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age: DF.Int
		department: DF.Literal["CSE", "IT", "MECH", "CIVIL", "AUTO"]
		email: DF.Data | None
		marks: DF.Float
		name1: DF.Data | None
		name: DF.Int | None
	# end: auto-generated types

	pass
