# Copyright (c) 2026, Thennarasu M and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Projectsemp(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		pro1: DF.Data | None
		pro2: DF.Data | None
	# end: auto-generated types

	pass
