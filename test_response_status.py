# Котеленец Еммануил, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import setup_order
import data

def test_status_of_order_is_200():
    response_order = setup_order.post_new_order(data.order_body_full) # 1 шаг - запрос на создание заказа
    track = {"t": response_order.json()["track"]} # 2 шаг - сохраняем номер трека заказа
    setup_order.getting_order_data(track) # 3 шаг - выполняем запрос на получение данных заказа по его треку
    response = setup_order.getting_order_data(track)
    assert response == 200 #Проверяем, равен ли код ответа 200