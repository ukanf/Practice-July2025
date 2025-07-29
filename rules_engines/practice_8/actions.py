# Define your action functions
def action_validate_inputs_in_input_data(context):
    # write to file or log
    print("Valid Input Data")
    return context

def action_validate_value_range_total_amount(context):
   # write to file or log
    print("Value in acceptable range")
    return context

def action_validate_paid_status(context):
    # write to file or log
    print("Paid status is valid")
    context['paid_status'] = 'Valid'
    return context

# Map action names to functions
ACTION_MAP = {
    'action_validate_inputs_in_input_data': action_validate_inputs_in_input_data,
    'action_validate_value_range_total_amount': action_validate_value_range_total_amount,
    'action_validate_paid_status': action_validate_paid_status,
}