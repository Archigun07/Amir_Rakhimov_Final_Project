# Амир Рахимов, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

# Выполение запроса на создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Получение заказа по номеру его трека
def get_order(track_number):
    get_order_track = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_track)
    return response

# Тест
def test_create_order_and_get_it_by_track():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print(track_number)

    order_response = get_order(track_number)
    assert order_response.status_code == 200
    order_data = order_response.json()
    print(order_data)