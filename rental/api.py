import frappe

@frappe.whitelist(allow_guest=True)
# @frappe.whitelist()
def get_emoji():
    return "🇰🇭"

def throw_emoji(doc, event):
    print("--"*20)
    print(doc)
    print(event)
    frappe.throw("🥹")

def send_payment_reminders():  
    print("Sending payment reminders...")

def get_query_conditions_for_vehicle(user):
    # frappe.throw(user)
    # return "name = 1"
    return ""
