from qr_demo.qr_code import get_qr_code
import frappe


@frappe.whitelist()
def qr_code():
    frappe.msgprint("hi")
    # doc=frappe.get_doc("Sales Invoice",current_doc)
    # no_data=0
    # qr_content ="HI"
    # # f'{doc.po_no,no_data,doc.customer,no_data,doc.posting_date,doc.name,doc.posting_date,doc.name,no_data,doc.total_qty,no_data,doc.total,doc.total,
    # #                 no_data,no_data,no_data,no_data,no_data,no_data,no_data,no_data,doc.grand_total}'
    # doc.custom_invoice_qr_detail = get_qr_code(qr_content)
    # doc.save()