# Котеленец Еммануил, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import order_create
import getting_order_data

def pos_assert_200(track): #позитивная проверка - проверяем, равен ли статус нашего запроса 200
    int_track = int(track)
    response = getting_order_data.getting_order_data(int_track)
    assert response == 200


def test_status_of_order_is_200():
    order_create.post_new_order() # 1 шаг - запрос на создание заказа
    track = order_create.get_order_track() # 2 шаг - сохраняем номер трека заказа
    getting_order_data.getting_order_data(track) # 3 шаг - выполняем запрос на получение данных заказа по его треку
    pos_assert_200(track) #Проверяем, равен ли код ответа 200