import config
import data
import requests
def post_new_order(order_body): # функция POST-запроса с созданием
    return requests.post(config.URL + config.ORDER_CREATE_PATH, json=order_body)
def get_order_track(order_body): #функция GET-запроса, в котором получаем трэк-номер заказа
    track = requests.post(config.URL + config.ORDER_CREATE_PATH, json=order_body)
    return track.json()['track']
def getting_order_data(track):
    response = requests.get(config.URL + config.GET_ORDER_DATA_PATH + '?t=' + str(track))
    return response.status_code