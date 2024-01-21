import config
import data
import requests
def post_new_order(): # функция POST-запроса с созданием
    new_order_body = data.order_body
    return requests.post(config.URL + config.ORDER_CREATE_PATH, json=new_order_body)
def get_order_track():
    track = requests.post(config.URL + config.ORDER_CREATE_PATH, json=data.order_body)
    return track.json()['track']
