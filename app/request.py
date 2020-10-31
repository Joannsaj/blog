import urllib.request,json
from .models import Quote

# Getting the base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_BASE_URL']


def get_quotes():

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        qoute_object = None

        if get_quotes_response:
            author = get_quotes_response.get('author')
            id = get_quotes_response.get('id')
            quote = get_quotes_response.get('quote')
            permalink = get_quotes_response.get('permalink')

            quote_object = Quote(author, id, quote, permalink)

    return quote_object

# def get_quotes():
#     '''
#     Function that gets the json response to our url request
#     '''
#     with urllib.request.urlopen(base_url) as url:
#         get_quotes_data = url.read()
#         get_quotes_response = json.loads(get_quotes_data)

#         quote_results = None

#         if get_quotes_response:
#             quote_results_list = get_quotes_response
#             quote_results = process_results(quote_results_list)


#     return quote_results

# def process_results(quote_list):
   
#     quote_results = []
#     for quote_item in quote_list:
#         author = quote_item.get('author')
#         id = quote_item.get('id')
#         quote = quote_item.get('quote')
#         permalink = quote_item.get('permalink')

#         quote_object = Quote(author, id, quote, permalink)
#         quote_results.append(quote_object)

#     return quote_results    