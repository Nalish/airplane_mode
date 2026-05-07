// Copyright (c) 2026, Sharon and contributors
// For license information, please see license.txt


frappe.ui.form.on('Airline', {
    refresh: function(frm) {

        // Avoid duplicate buttons
        frm.clear_custom_buttons();

        // Only show if website exists
        if (frm.doc.website) {

            frm.add_custom_button('Visit Website', () => {
                window.open(frm.doc.website, '_blank');
            });

        }
    }
});
