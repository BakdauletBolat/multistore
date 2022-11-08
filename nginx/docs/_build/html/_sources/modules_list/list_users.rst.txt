Получение пользователей 🏪
========================================




.. function:: Сделайте запрос методом `GET` по ссылке: api/v1/users/


.. note::
   Данный запрос отправляет ответ со списками пользователей

   Значение **search** для поиска пользователей, 


**Успешный запрос:**

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

   {
    "links": {
        "first": "http://127.0.0.1:8001/api/v1/users/?page%5Bnumber%5D=1",
        "last": "http://127.0.0.1:8001/api/v1/users/?page%5Bnumber%5D=57",
        "next": "http://127.0.0.1:8001/api/v1/users/?page%5Bnumber%5D=2",
        "prev": null
    },
    "data": [
        {
            "type": "Author",
            "id": "1",
            "attributes": {
                "full_name": "Super Admin",
                "role_id": 2
            }
        },
        {
            "type": "Author",
            "id": "2",
            "attributes": {
                "full_name": "Auth Service",
                "role_id": 4
            }
        },
        {
            "type": "Author",
            "id": "3",
            "attributes": {
                "full_name": "IMS Service",
                "role_id": 4
            }
        },
        {
            "type": "Author",
            "id": "4",
            "attributes": {
                "full_name": "Prices Service",
                "role_id": 4
            }
        },
        {
            "type": "Author",
            "id": "5",
            "attributes": {
                "full_name": "Питер",
                "role_id": 5
            }
        },
        {
            "type": "Author",
            "id": "6",
            "attributes": {
                "full_name": "Паркер",
                "role_id": 5
            }
        },
        {
            "type": "Author",
            "id": "7",
            "attributes": {
                "full_name": "Exchange Online-ApplicationAccount",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "8",
            "attributes": {
                "full_name": "LyncEnterprise-ApplicationAccount",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "9",
            "attributes": {
                "full_name": "Служба поддержки",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "10",
            "attributes": {
                "full_name": "Гость",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "11",
            "attributes": {
                "full_name": "Администратор",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "12",
            "attributes": {
                "full_name": "krbtgt",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "13",
            "attributes": {
                "full_name": "Расим Димухамедов",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "14",
            "attributes": {
                "full_name": "Ержан Абдухаимов",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "15",
            "attributes": {
                "full_name": "Admin05",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "16",
            "attributes": {
                "full_name": "Музаффар Халыкназаров",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "17",
            "attributes": {
                "full_name": "Admin06",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "18",
            "attributes": {
                "full_name": "Нурбек Кулыбеков",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "19",
            "attributes": {
                "full_name": "Данил Хегай",
                "role_id": null
            }
        },
        {
            "type": "Author",
            "id": "20",
            "attributes": {
                "full_name": "admin1",
                "role_id": null
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 57,
            "count": 1131
        }
    }
}