# Copyright (c) 2026, Thennarasu M and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils import *
# @frappe.whitelist()
# def utility():
	#return now();
	#return getdate();
	#return today();
	#tdy = today();
	#tdy = add_to_date(tdy,days=10,years=1,months=5);
	# date1 = today()
	# date2 = add_to_date(date1,years=-10)
	# res = date_diff(date2,date1)
	#return date_diff(add_to_date(today(),years=-1),today());
	#res=days_diff(date1,date2);
	#return res;
	#return pretty_date(now())
	#return format_duration(10000000);
	#return comma_and([1,2,3]);
	#return comma_or([1,2,3]);
	#return money_in_words(10000,"USD")
# @frappe.whitelist()
# def utility2():
    # try:
    #     validate_json_string('{name":"abcd"}')
    #     return True
    # except frappe.ValidationError:
    #     return False
	#return mask_string("1234567890", mask_char="#", show_first=2, show_last=2)
	#return mask_string("1234567890");// not working
	#return unique('12341');
	#return get_abbr("Abc D")
	# try:
	# 	validate_url('https://google.com')
	# 	return True
	# except frappe.ValidationError:
	# 	return False
	# try:
	# 	return validate_email_address('example@gmail..com.comcom')
	# except frappe.ValidationError:
	# 	return False
	# try:
	# 	return validate_phone_number('inv')
	# except frappe.ValidationError:
	# 	return False
class EmployeeManagement(Document):
	
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from library_management.library_tech.doctype.projectsemp.projectsemp import Projectsemp

		active: DF.Check
		bonus: DF.Currency
		department: DF.Literal["HR", "IT", "SALES", "FINANCE"]
		designation: DF.Data | None
		dob: DF.Date | None
		email: DF.Data | None
		experience: DF.Int
		id: DF.Data | None
		joining: DF.Datetime | None
		links: DF.Link | None
		name1: DF.Data | None
		name: DF.Int | None
		phone: DF.Phone | None
		salary: DF.Currency
		table1: DF.Table[Projectsemp]
		total_salary: DF.Currency
	# end: auto-generated types

	# @frappe.whitelist()
	# def get_doc(self):
	# 	return self.name1
	# @frappe.whitelist()
	# def func(self):
	# 	doc = frappe.get_doc("Employee Management",7)
	# 	doc = frappe.get_last_doc("Employee Management"); #filters,
	# 	doc = frappe.new_doc("Employee Management");
	# 	doc.name1="check1";
	# 	doc.insert();
	# 	doc = frappe.delete_doc("Employee Management",8);
	# 	doc =  frappe.rename_doc("Employee Management",1,10);
	# 	doc = frappe.get_meta("Employee Management")
	# 	return doc.name
	# @frappe.whitelist()
	# def onlyfor(self):
	# 	frappe.msgprint("Line 1");
	# 	frappe.only_for("System Manager");
	# 	frappe.msgprint("Admin Line");
	# def updates(self):
	# 	doc = frappe.get_doc("Employee Management",7);
	# 	doc.name1="Changed"
	# 	doc.save()
	# @frappe.whitelist()
	# def validate(self):
	# 	old_doc = self.get_doc_before_save()

	# 	if old_doc and self.name1 != old_doc.name1:
	# 		frappe.msgprint("Changed")
	# 		frappe.utils.play_sound("ping")
	# 	val = self.has_value_changed("name1");
	# 	title = self.get_title();
	# 	frappe.msgprint(title);
	# 	if val:
	# 		frappe.msgprint("field value changed");
		
	# @frappe.whitelist()
	# def func1(self):
	# 	doc = frappe.get_doc("Employee Management",7);
	# 	doc.name1="nu";
	# 	doc.save();
	# 	# doc.notify_update();
	# 	doc.append("table1",{
	# 		"pro1":"a1",
	# 		"pro2":"a2"
	# 	})
	# 	doc.save();
	# 	doc.set("name1","dbset");
	# 	doc.save();
	# 	url=doc.get_url();
	# 	frappe.msgprint(url);
	# 	doc.add_comment('Comment',text='Test Comment');
	# @frappe.whitelist()
	# def func2(self):
	# 	doc = frappe.get_doc("Employee Management",7)
	# 	doc.add_tag("Important")
	# 	tags = doc.get_tags()
	# 	return tags
	# def test(self):
	# 	return "donee!!"
	# @frappe.whitelist()
	# def runmethod(self):
	# 	doc = frappe.get_doc("Employee Management",7)
	# 	result = doc.run_method("test");
	# 	return result
	# @frappe.whitelist()
	# def parent(self):
	# 	doc =frappe.get_doc("Employee Management",7);
	# 	child = doc.get_children();
	# 	return child
	# @frappe.whitelist()
	# def dbdot(self):
	# 	doc =frappe.get_doc("Employee Management",7);
	# 	doc.name1="dbdotchanged";
	# 	doc.db_update();
	# 	doc=frappe.new_doc("Employee Management");
	# 	doc.name1="dbdotinsert";
	# 	doc.db_insert();
	# frappe.publish_progress(25, title='Some title', description='Some description')



		

