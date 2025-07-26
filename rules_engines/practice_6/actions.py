# Define your action functions
def action_flag_rich_minor(context):
    context['flag'] = 'suspicious'
    context['note'] = 'Minor with high income'
    return context

def action_reject_minor(context):
    context['eligible'] = False
    context['message'] = 'Rejected due to age'
    return context

def action_approve_adult_with_income(context):
    context['eligible'] = True
    context['message'] = 'Approved based on age and income'
    return context

def action_reject_older_adult(context):
    context['eligible'] = False
    context['message'] = 'Rejected due to age'
    return context

# Map action names to functions
ACTION_MAP = {
    'action_flag_rich_minor': action_flag_rich_minor,
    'action_reject_minor': action_reject_minor,
    'action_approve_adult_with_income': action_approve_adult_with_income,
    'action_reject_older_adult': action_reject_older_adult,
}