# Copyright (c) 2026, Sharon and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

   

    def validate(self):
        self.calculate_total_amount()
        self.remove_duplicate_addons()

    def calculate_total_amount(self):
        total = self.flight_price or 0

        for row in self.add_ons:
            amount = row.amount or 0
            total += amount

        self.total_amount = total
    
    def remove_duplicate_addons(self):
        seen=set()
        unique_rows=[]
        for row in self.add_ons:
            if row.item not in seen:
                seen.add(row.item)
                unique_rows.append(row)
            else:
                frappe.msgprint(
                    f"Duplicate add-on '{row.item}' removed automatically",
                    alert=True
                )
        self.add_ons =unique_rows

    def before_submit(self):
        self.check_status()


    def before_insert(self):
        self.generate_seat()

    def check_status(self):
        if self.status != "Boarded":
            frappe.throw("You can only submit if status is Boarded")

    def generate_seat(self):
        number=random.randint(1,99)
        letter=random.choice(["A","B","C","D","E"])

        self.seat=f"{number}{letter}"
