Качествы товара 🏢
========================================


.. function:: Сделайте запрос методом `GET` по ссылке: /api/v1/handbook/qualities/


.. note::
   Данная запрос отправляет ответ список качеств товара


**Успешный запрос:**

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json
{
    "links": {
        "first": "http://127.0.0.1:8000/api/v1/handbook/qualities/?page%5Bnumber%5D=1",
        "last": "http://127.0.0.1:8000/api/v1/handbook/qualities/?page%5Bnumber%5D=1",
        "next": null,
        "prev": null
    },
    "data": [
        {
            "type": "Quality",
            "id": "1",
            "attributes": {
                "uid": "5541eee7-f450-11e2-baeb-001e670c9280",
                "name": "Брак"
            }
        },
        {
            "type": "Quality",
            "id": "2",
            "attributes": {
                "uid": "6574b5da-6753-11e1-9495-001a6bb697cb",
                "name": "Дефект"
            }
        },
        {
            "type": "Quality",
            "id": "3",
            "attributes": {
                "uid": "d05404a0-6bce-449b-a798-41ebe5e5b977",
                "name": "Новый"
            }
        },
        {
            "type": "Quality",
            "id": "4",
            "attributes": {
                "uid": "00c425e9-2802-11eb-80c2-bc97e145c062",
                "name": "Отремонтированный"
            }
        },
        {
            "type": "Quality",
            "id": "5",
            "attributes": {
                "uid": "04880e3d-6819-11ea-a204-20040ff8c2a0",
                "name": "Распакованный"
            }
        },
        {
            "type": "Quality",
            "id": "6",
            "attributes": {
                "uid": "c5c7e039-b9f7-11eb-80cb-bc97e145c062",
                "name": "Торговый зал"
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 1,
            "count": 6
        }
    }
}