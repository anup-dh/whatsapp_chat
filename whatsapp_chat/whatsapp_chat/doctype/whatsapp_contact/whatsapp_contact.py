# Copyright (c) 2024, shridhar patil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WhatsAppContact(Document):

	def after_insert(self):
		if self.email:
			frappe.publish_realtime(
				"new_room_creation", 
				{
					"user": self.email,  
					"room_name": self.contact_name
				}, 
				user=self.email
			)

	pass
