# Define your action functions
def action_approve_utilization_customerage(context):
    context['decision'] = 'Approve'
    # context['utilization'] = ''
    # context['available'] = ''
    return context

def action_approve_utilization_newcustomer(context):
    context['decision'] = 'Approve'
    # context['utilization'] = ''
    # context['available'] = ''
    return context

def action_refer_utilization(context):
    context['decision'] = 'Refer'
    # context['utilization'] = ''
    # context['available'] = ''
    return context

def action_decline_utilization(context):
    context['decision'] = 'Decline'
    # context['utilization'] = ''
    # context['available'] = ''
    return context

def action_alwaysrefer_customer(context):
    context['decision'] = 'Refer'
    # context['utilization'] = ''
    # context['available'] = ''
    return context


# Map action names to functions
ACTION_MAP = {
    'action_approve_utilization_customerage': action_approve_utilization_customerage,
    'action_approve_utilization_newcustomer': action_approve_utilization_newcustomer,
    'action_refer_utilization': action_refer_utilization,
    'action_decline_utilization': action_decline_utilization,
    'action_alwaysrefer_customer': action_alwaysrefer_customer
}