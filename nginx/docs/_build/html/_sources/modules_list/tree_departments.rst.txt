Получение tree departments 🏪
========================================




.. function:: Сделайте запрос методом `GET` по ссылке: api/v1/handbook/departments/


.. note::
   Данная запрос отправляет ответ список подразделений


**Успешный запрос:**

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
    "links": {
        "first": "http://127.0.0.1:8000/api/v1/handbook/departments/?page%5Bnumber%5D=1",
        "last": "http://127.0.0.1:8000/api/v1/handbook/departments/?page%5Bnumber%5D=1",
        "next": null,
        "prev": null
    },
    "data": [
        {
            "type": "Department",
            "id": "187",
            "attributes": {
                "name": "Алматы",
                "children": [
                    {
                        "id": 182,
                        "name": "Алматы Ритц Палас",
                        "children": []
                    }
                ]
            }
        },
        {
            "type": "Department",
            "id": "188",
            "attributes": {
                "name": "Внутренний сервис",
                "children": []
            }
        },
        {
            "type": "Department",
            "id": "189",
            "attributes": {
                "name": "Нур Султан",
                "children": [
                    {
                        "id": 163,
                        "name": "Грин Молл",
                        "children": []
                    }
                ]
            }
        },
        {
            "type": "Department",
            "id": "190",
            "attributes": {
                "name": "Караганда",
                "children": []
            }
        },
        {
            "type": "Department",
            "id": "191",
            "attributes": {
                "name": "Алматинская область",
                "children": [
                    {
                        "id": 159,
                        "name": "Жаркент",
                        "children": []
                    },
                    {
                        "id": 160,
                        "name": "Отеген Батыр",
                        "children": []
                    },
                    {
                        "id": 161,
                        "name": "Узынагаш",
                        "children": []
                    },
                    {
                        "id": 162,
                        "name": "Каскелен",
                        "children": []
                    }
                ]
            }
        },
        {
            "type": "Department",
            "id": "192",
            "attributes": {
                "name": "Шымкент",
                "children": [
                    {
                        "id": 11,
                        "name": "Шымкент Жангельдина",
                        "children": []
                    },
                    {
                        "id": 12,
                        "name": "Шымкент Рыскулова",
                        "children": []
                    },
                    {
                        "id": 13,
                        "name": "Шымкент Янги-Шахар",
                        "children": []
                    },
                    {
                        "id": 14,
                        "name": "Шымкент Акбар",
                        "children": []
                    }
                ]
            }
        },
        {
            "type": "Department",
            "id": "193",
            "attributes": {
                "name": "Жамбылская область",
                "children": [
                    {
                        "id": 15,
                        "name": "Тараз-Алатау",
                        "children": []
                    },
                    {
                        "id": 16,
                        "name": "Шу",
                        "children": []
                    },
                    {
                        "id": 17,
                        "name": "Тараз Mall",
                        "children": []
                    },
                    {
                        "id": 18,
                        "name": "Сарыкемер",
                        "children": []
                    },
                    {
                        "id": 19,
                        "name": "Тараз Сатпаева",
                        "children": []
                    }
                ]
            }
        },
        {
            "type": "Department",
            "id": "194",
            "attributes": {
                "name": "Туркестанская область",
                "children": [
                    {
                        "id": 20,
                        "name": "Казыгурт",
                        "children": []
                    },
                    {
                        "id": 21,
                        "name": "Тулькубас",
                        "children": []
                    },
                    {
                        "id": 22,
                        "name": "Жетысай",
                        "children": []
                    },
                    {
                        "id": 23,
                        "name": "Туркестан",
                        "children": []
                    },
                    {
                        "id": 24,
                        "name": "Сарыагаш",
                        "children": []
                    },
                    {
                        "id": 25,
                        "name": "Аксукент",
                        "children": []
                    },
                    {
                        "id": 26,
                        "name": "Туркестан-Rixos",
                        "children": []
                    },
                    {
                        "id": 27,
                        "name": "Арысь",
                        "children": []
                    },
                    {
                        "id": 28,
                        "name": "Ленгер",
                        "children": []
                    },
                    {
                        "id": 29,
                        "name": "Карабулак",
                        "children": []
                    }
                ]
            }
        },
        {
            "type": "Department",
            "id": "195",
            "attributes": {
                "name": "Кызылординская область",
                "children": [
                    {
                        "id": 95,
                        "name": "Кызылорда",
                        "children": []
                    },
                    {
                        "id": 96,
                        "name": "Айтеке Би",
                        "children": []
                    },
                    {
                        "id": 97,
                        "name": "Торетам",
                        "children": []
                    },
                    {
                        "id": 98,
                        "name": "Шиели",
                        "children": []
                    },
                    {
                        "id": 99,
                        "name": "Аральск",
                        "children": []
                    }
                ]
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 1,
            "count": 9
        }
    }
}