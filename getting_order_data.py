import requests
import config

def getting_order_data(track):
    response = requests.get(config.URL + config.GET_ORDER_DATA_PATH + '?t=' + track)
    print(config.URL + config.GET_ORDER_DATA_PATH + '?t=', track)
    return response.status_code

getting_order_data(171782)