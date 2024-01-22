import config
import data
import requests
def post_new_order(): # функция POST-запроса с созданием
    new_order_body = data.order_body.copy()
    new_order_body ['firstName'] = 'Имя' #Только русские буквы, пробел, тире. Длина не менее 2 и не более 15 символов.
    new_order_body ['lastName'] = 'Фамилия' #Только русские буквы. Длина не менее 2 и не более 15 символов.
    new_order_body ['address'] = 'Адрес, дом 69' #Только русские буквы, цифры, пробел, тире, точка, запятая. Длина не менее 5 и не более 50 символов.
    new_order_body ['metroStation'] = '69' #Номер станции метро (узнается запросом на бэкенд
    new_order_body ['phone'] = '+79852992929' #Только цифры и знак +. Длина не менее 10 и не более 12 символов.
    new_order_body ['rentTime'] = '4' #Кол-во суток, от 1 до 7
    new_order_body ['deliveryDate'] = '2024-01-30' #Дата заказа, в формате гггг-мм-дд
    new_order_body ['comment'] = 'привет!' #Только русские буквы, цифры, пробел, тире, точка, запятая. Длина не более 24 символов.
    new_order_body ['color'] = ['BLACK'] #Либо ['BLACK'], либо ['WHITE']. Либо пустое поле оставить
    return requests.post(config.URL + config.ORDER_CREATE_PATH, json=new_order_body)
def get_order_track(): #функция GET-запроса, в котором получаем трэк-номер заказа
    new_order_body = data.order_body.copy()
    new_order_body['firstName'] = 'Имя'  # Только русские буквы, пробел, тире. Длина не менее 2 и не более 15 символов.
    new_order_body['lastName'] = 'Фамилия'  # Только русские буквы. Длина не менее 2 и не более 15 символов.
    new_order_body['address'] = 'Адрес, дом 69'  # Только русские буквы, цифры, пробел, тире, точка, запятая. Длина не менее 5 и не более 50 символов.
    new_order_body['metroStation'] = '69'  # Номер станции метро (узнается запросом на бэкенд
    new_order_body['phone'] = '+79852992929'  # Только цифры и знак +. Длина не менее 10 и не более 12 символов.
    new_order_body['rentTime'] = '4'  # Кол-во суток, от 1 до 7
    new_order_body['deliveryDate'] = '2024-01-30'  # Дата заказа, в формате гггг-мм-дд
    new_order_body['comment'] = 'привет!'  # Только русские буквы, цифры, пробел, тире, точка, запятая. Длина не более 24 символов.
    new_order_body['color'] = ['BLACK']  # Либо ['BLACK'], либо ['WHITE']. Либо пустое поле оставить
    track = requests.post(config.URL + config.ORDER_CREATE_PATH, json=new_order_body)
    return track.json()['track']