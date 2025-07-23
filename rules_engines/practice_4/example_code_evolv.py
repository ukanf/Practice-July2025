from practice_4.rules_engine import Rule, RulesEngine


def handle_1(response):
    if response.status_code == 204:
        return []
    elif response.status_code in [401, 403]:
        raise NoAccessError(response.text)
    elif response.status_code == 404:
        if response.url.startswith("https://api.github.com/repos/"):
            return []
    response.raise_for_status()
    return response.json()

# flattened version
def handle_2(response):
    if response.status_code == 204:
        return []
    elif response.status_code in [401, 403]:
        raise NoAccessError(response.text)
    elif response.status_code == 404 and response.url.startswith("https://api.github.com/repos/"):
        return []
    else:
        response.raise_for_status()
        return response.json()
    
# now we start creating methods for each status code
def empty_response():
    return []

def no_data(response):
    return response.status_code == 204

def access_denied(response):
    return response.status_code in [401, 403]

def access_error(response):
    raise NoAccessError(response.text)

def optional_data_not_found(response):
    return not_found(response) and optional_data(response)

def optional_data(response):
    return response.url.startswith("https://api.github.com/repos/")

def not_found(response):
    return response.status_code == 404

def process_response(response):
    response.raise_for_status()
    return response.json()

def otherwise():
    return True

def handle_2(response):
    if no_data(response):
        return empty_response()
    elif access_denied(response):
        access_error(response)
    elif optional_data_not_found(response):
        return empty_response()
    elif otherwise:
        return process_response(response)
    
# converting it into rules:
def handle_3(response):
    return RulesEngine([
        Rule("No Data", no_data, empty_response),
        Rule("Access Denied", access_denied, access_error),
        Rule("Optional Data Not Found", optional_data_not_found, empty_response),
        Rule("Otherwise", otherwise, process_response)
    ]).run(response)