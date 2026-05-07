# Copyright (c) 2026, Sharon and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Airline(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		airline_name: DF.Data | None
		customer_care_number: DF.Data
		founding_year: DF.Int
		headquaters: DF.Data
		is_published: DF.Check
		route: DF.Data | None
		website: DF.Data | None
	# end: auto-generated types

	pass
