Получение пользователей 🏪
========================================




.. function:: Сделайте запрос методом `GET` по ссылке: api/v1/ebm-users/


.. note::
   Данный запрос отправляет ответ со списками клиентов


   Значение **search** для поиска клиентов,

    Search будет искать по следющам ключам
    **name**, **surname**, **phone**


**Успешный запрос:**

*Ответ*::

   - Status: 200 OK


*Дата данные*:

.. code-block:: json

   {
    "links": {
        "first": "http://127.0.0.1:8000/api/v1/ebm-users/",
        "last": "http://127.0.0.1:8000/api/v1/ebm-users/",
        "next": "http://127.0.0.1:8000/api/v1/ebm-users/",
        "prev": null
    },
    "data": [
        {
            "type": "EUser",
            "id": "1",
            "attributes": {
                "name": "Евгений",
                "ebm_user_id": 4,
                "surname": "Козачинский",
                "phone": "77467457457"
            }
        },
        {
            "type": "EUser",
            "id": "2",
            "attributes": {
                "name": "Артем",
                "ebm_user_id": 8,
                "surname": "Wezom",
                "phone": "71234567890"
            }
        },
        {
            "type": "EUser",
            "id": "3",
            "attributes": {
                "name": "Миржан",
                "ebm_user_id": 16,
                "surname": "Ибрагимов",
                "phone": "77025400055"
            }
        },
        {
            "type": "EUser",
            "id": "4",
            "attributes": {
                "name": "Индира",
                "ebm_user_id": 168,
                "surname": "Козиева",
                "phone": "77028883065"
            }
        },
        {
            "type": "EUser",
            "id": "5",
            "attributes": {
                "name": "Боранбаев",
                "ebm_user_id": 263,
                "surname": "Ермек",
                "phone": "77015186050"
            }
        },
        {
            "type": "EUser",
            "id": "6",
            "attributes": {
                "name": "Рахимбердиев",
                "ebm_user_id": 329,
                "surname": "Бегали",
                "phone": "77011874770"
            }
        },
        {
            "type": "EUser",
            "id": "7",
            "attributes": {
                "name": "Шерметов",
                "ebm_user_id": 1256,
                "surname": "Руслан",
                "phone": "77056999333"
            }
        },
        {
            "type": "EUser",
            "id": "8",
            "attributes": {
                "name": "Марат",
                "ebm_user_id": 1317,
                "surname": "Джарасов",
                "phone": "77017869056"
            }
        },
        {
            "type": "EUser",
            "id": "9",
            "attributes": {
                "name": "Еркин",
                "ebm_user_id": 1936,
                "surname": "Данияров",
                "phone": "77028000707"
            }
        },
        {
            "type": "EUser",
            "id": "10",
            "attributes": {
                "name": "Кулсин",
                "ebm_user_id": 2031,
                "surname": "Касымбекова",
                "phone": "77071670967"
            }
        },
        {
            "type": "EUser",
            "id": "11",
            "attributes": {
                "name": "Нурмахан",
                "ebm_user_id": 2505,
                "surname": "Асылханулы",
                "phone": "77055553519"
            }
        },
        {
            "type": "EUser",
            "id": "12",
            "attributes": {
                "name": "Мафтуна",
                "ebm_user_id": 2642,
                "surname": "Камалова",
                "phone": "77076518710"
            }
        },
        {
            "type": "EUser",
            "id": "13",
            "attributes": {
                "name": "Еркебулан ",
                "ebm_user_id": 2706,
                "surname": "Парманкулов ",
                "phone": "77083121712"
            }
        },
        {
            "type": "EUser",
            "id": "14",
            "attributes": {
                "name": "Грошев",
                "ebm_user_id": 2840,
                "surname": "Виктор",
                "phone": "77029674656"
            }
        },
        {
            "type": "EUser",
            "id": "15",
            "attributes": {
                "name": "Ахрорали",
                "ebm_user_id": 3896,
                "surname": "Камбаралиев",
                "phone": "77786888879"
            }
        },
        {
            "type": "EUser",
            "id": "16",
            "attributes": {
                "name": "Дмитрий",
                "ebm_user_id": 4155,
                "surname": "Ли",
                "phone": "77078703017"
            }
        },
        {
            "type": "EUser",
            "id": "17",
            "attributes": {
                "name": "Игорь",
                "ebm_user_id": 4347,
                "surname": "Кангур",
                "phone": "77716840666"
            }
        },
        {
            "type": "EUser",
            "id": "18",
            "attributes": {
                "name": "КАЗИ ",
                "ebm_user_id": 4361,
                "surname": "ТАЖИБАЕВ",
                "phone": "77056828857"
            }
        },
        {
            "type": "EUser",
            "id": "19",
            "attributes": {
                "name": "Туребеков",
                "ebm_user_id": 4470,
                "surname": "Ергеш",
                "phone": "77719144551"
            }
        },
        {
            "type": "EUser",
            "id": "20",
            "attributes": {
                "name": "Гайдаров",
                "ebm_user_id": 5012,
                "surname": "Дамир",
                "phone": "77786530181"
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 103,
            "count": 2054
        }
    }
}