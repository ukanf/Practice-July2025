# custom_rules.py

def check_vip(context):
    if context.get("vip_code") == "X123":
        context["is_vip"] = True
