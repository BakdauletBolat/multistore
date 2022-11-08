Получение городов 🏢
========================================



API для получения списка акций по id

.. function:: Сделайте запрос методом `GET` по ссылке: /api/v1/handbook/cities/


.. note::
   Данная запрос отправляет ответ список городов


**Успешный запрос:**

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
    "links": {
        "first": "http://127.0.0.1:8000/api/v1/handbook/cities/?page%5Bnumber%5D=1",
        "last": "http://127.0.0.1:8000/api/v1/handbook/cities/?page%5Bnumber%5D=1",
        "next": null,
        "prev": null
    },
    "data": [
        {
            "type": "City",
            "id": "1",
            "attributes": {
                "name": "Шымкент",
                "uid": "0952aa95-c71c-11ea-80bf-bc97e145c061",
                "shops": [
                    {
                        "id": 1,
                        "name": "Шымкент Рыскулова",
                        "uid": "f3fb7bbf-547f-11e1-a65d-001fd0a3d61d"
                    },
                    {
                        "id": 2,
                        "name": "Шымкент Жангельдина",
                        "uid": "f3fb7bc1-547f-11e1-a65d-001fd0a3d61d"
                    },
                    {
                        "id": 3,
                        "name": "Шымкент Янги-Шахар",
                        "uid": "3f733259-8f01-11e8-80e7-1866da78d386"
                    },
                    {
                        "id": 4,
                        "name": "Шымкент Акбар",
                        "uid": "f5899ebe-a140-11e8-80e9-1866da78d386"
                    }
                ]
            }
        },
        {
            "type": "City",
            "id": "2",
            "attributes": {
                "name": "Нур-Султан",
                "uid": "10ee743a-c71c-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "3",
            "attributes": {
                "name": "Алматы",
                "uid": "1730f034-c71c-11ea-80bf-bc97e145c061",
                "shops": [
                    {
                        "id": 29,
                        "name": "Грин Молл",
                        "uid": "f0ba3532-c756-11eb-80cd-bc97e145c062"
                    },
                    {
                        "id": 30,
                        "name": "Алматы Ритц Палас",
                        "uid": "9b26a475-9bb5-11e8-80e9-1866da78d386"
                    }
                ]
            }
        },
        {
            "type": "City",
            "id": "4",
            "attributes": {
                "name": "Туркестанская область",
                "uid": "fa87d150-c71a-11ea-80bf-bc97e145c061",
                "shops": [
                    {
                        "id": 10,
                        "name": "Арысь",
                        "uid": "50cea639-49d8-11e8-80de-1866da78d386"
                    },
                    {
                        "id": 11,
                        "name": "Ленгер",
                        "uid": "c24c1e70-7448-11e8-80e4-1866da78d386"
                    },
                    {
                        "id": 12,
                        "name": "Туркестан-Rixos",
                        "uid": "51f4add8-65f9-11eb-80c5-bc97e145c062"
                    },
                    {
                        "id": 13,
                        "name": "Карабулак",
                        "uid": "e78f99f3-cfea-11ea-80bf-bc97e145c061"
                    },
                    {
                        "id": 14,
                        "name": "Казыгурт",
                        "uid": "f7760885-6ff9-11ea-a205-20040ff8c2a0"
                    },
                    {
                        "id": 15,
                        "name": "Тулькубас",
                        "uid": "97617a1e-4d55-11ea-a204-20040ff8c2a0"
                    },
                    {
                        "id": 16,
                        "name": "Сарыагаш",
                        "uid": "f696b05f-def5-11e2-a747-001e670c9280"
                    },
                    {
                        "id": 17,
                        "name": "Аксукент",
                        "uid": "fbb1d90e-250f-11e3-a8b4-001e670c9280"
                    },
                    {
                        "id": 18,
                        "name": "Жетысай",
                        "uid": "5ffdd76c-c548-11e3-b70c-001e670c9280"
                    },
                    {
                        "id": 19,
                        "name": "Туркестан",
                        "uid": "5ffdd76d-c548-11e3-b70c-001e670c9280"
                    }
                ]
            }
        },
        {
            "type": "City",
            "id": "5",
            "attributes": {
                "name": "Аксукент",
                "uid": "a44a73f7-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "6",
            "attributes": {
                "name": "Жетысай",
                "uid": "a44a73f8-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "7",
            "attributes": {
                "name": "Туркестан",
                "uid": "adb3186a-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "8",
            "attributes": {
                "name": "Арысь",
                "uid": "b892a7c5-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "9",
            "attributes": {
                "name": "Казыгурт",
                "uid": "c1304509-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "10",
            "attributes": {
                "name": "Кентау",
                "uid": "c130450a-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "11",
            "attributes": {
                "name": "Ленгер",
                "uid": "ca9ffa05-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "12",
            "attributes": {
                "name": "Сарыагаш",
                "uid": "ddce1603-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "13",
            "attributes": {
                "name": "Шардара",
                "uid": "ebaceaea-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "14",
            "attributes": {
                "name": "Тулькубас",
                "uid": "9f5267e3-c74d-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "15",
            "attributes": {
                "name": "Карабулак",
                "uid": "2e39ac36-d083-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "16",
            "attributes": {
                "name": "Атырауская область",
                "uid": "1a1ec511-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "17",
            "attributes": {
                "name": "Атырау",
                "uid": "4ff479f9-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "18",
            "attributes": {
                "name": "Кульсары",
                "uid": "562b285a-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "19",
            "attributes": {
                "name": "Актюбинская область",
                "uid": "21e3b798-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "20",
            "attributes": {
                "name": "Актобе",
                "uid": "9d86b28b-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "21",
            "attributes": {
                "name": "Кызылординская область",
                "uid": "2bd1e58d-c71b-11ea-80bf-bc97e145c061",
                "shops": [
                    {
                        "id": 20,
                        "name": "Кызылорда",
                        "uid": "c2ce6d90-ecaa-11e8-80ee-1866da78d386"
                    },
                    {
                        "id": 21,
                        "name": "Айтеке Би",
                        "uid": "905cfd49-059e-11ec-80d0-bc97e145c062"
                    },
                    {
                        "id": 22,
                        "name": "Торетам",
                        "uid": "270fffd7-a8d5-11eb-80c9-bc97e145c062"
                    },
                    {
                        "id": 23,
                        "name": "Шиели",
                        "uid": "a04ca64e-e2cb-11eb-80cd-bc97e145c062"
                    },
                    {
                        "id": 24,
                        "name": "Аральск",
                        "uid": "20983e44-cbe0-11ea-80bf-bc97e145c061"
                    }
                ]
            }
        },
        {
            "type": "City",
            "id": "22",
            "attributes": {
                "name": "Кызылорда",
                "uid": "50682b6c-c71c-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "23",
            "attributes": {
                "name": "Аральск",
                "uid": "4e61ef68-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "24",
            "attributes": {
                "name": "Байконур",
                "uid": "5487d311-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "25",
            "attributes": {
                "name": "Казалинск",
                "uid": "6b560b6e-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "26",
            "attributes": {
                "name": "Шиели",
                "uid": "74d02aa0-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "27",
            "attributes": {
                "name": "Торетам",
                "uid": "3a51c77d-b223-11eb-80cb-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "28",
            "attributes": {
                "name": "Мангистауская область",
                "uid": "32d334f1-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "29",
            "attributes": {
                "name": "Актау",
                "uid": "25520bd3-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "30",
            "attributes": {
                "name": "Жанаозен",
                "uid": "318faeb4-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "31",
            "attributes": {
                "name": "Бейнеу",
                "uid": "de4276b9-f251-11ea-80c0-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "32",
            "attributes": {
                "name": "Павлодарская область",
                "uid": "3d3897ad-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "33",
            "attributes": {
                "name": "Аксу",
                "uid": "fbfcf9ec-c770-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "34",
            "attributes": {
                "name": "Павлодар",
                "uid": "149b04d9-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "35",
            "attributes": {
                "name": "Экибастуз",
                "uid": "1b1c5a2d-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "36",
            "attributes": {
                "name": "Костанайская область",
                "uid": "44d74b5e-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "37",
            "attributes": {
                "name": "Костанай",
                "uid": "91b4372d-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "38",
            "attributes": {
                "name": "Лисаковск",
                "uid": "97d0aad0-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "39",
            "attributes": {
                "name": "Рудный",
                "uid": "97d0aad1-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "40",
            "attributes": {
                "name": "Акмолинская область",
                "uid": "5fb9d55a-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "41",
            "attributes": {
                "name": "Кокшетау (Көкшетау)",
                "uid": "0a038ad2-c773-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "42",
            "attributes": {
                "name": "Степногорск (Степногорск)",
                "uid": "1a432a96-c773-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "43",
            "attributes": {
                "name": "Щучинск",
                "uid": "e8b44784-f252-11ea-80c0-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "44",
            "attributes": {
                "name": "Алматинская область",
                "uid": "6709e712-c71b-11ea-80bf-bc97e145c061",
                "shops": [
                    {
                        "id": 25,
                        "name": "Жаркент",
                        "uid": "fc61cf8b-e1da-11ea-80bf-bc97e145c061"
                    },
                    {
                        "id": 26,
                        "name": "Отеген Батыр",
                        "uid": "d3f25785-059d-11ec-80d0-bc97e145c062"
                    },
                    {
                        "id": 27,
                        "name": "Узынагаш",
                        "uid": "17c372e3-825c-11eb-80c7-bc97e145c062"
                    },
                    {
                        "id": 28,
                        "name": "Каскелен",
                        "uid": "95ee3e30-bc48-11ea-80bf-bc97e145c061"
                    }
                ]
            }
        },
        {
            "type": "City",
            "id": "45",
            "attributes": {
                "name": "Каскелен",
                "uid": "bb7c9c45-c76f-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "46",
            "attributes": {
                "name": "Есик",
                "uid": "62a956b2-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "47",
            "attributes": {
                "name": "Жаркент",
                "uid": "6a51911e-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "48",
            "attributes": {
                "name": "Капшагай",
                "uid": "70968dec-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "49",
            "attributes": {
                "name": "Талгар",
                "uid": "7d3a99ad-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "50",
            "attributes": {
                "name": "Талдыкорган",
                "uid": "83f45ba0-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "51",
            "attributes": {
                "name": "Текели",
                "uid": "83f45ba1-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "52",
            "attributes": {
                "name": "Узынагаш",
                "uid": "879d29d7-825c-11eb-80c7-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "53",
            "attributes": {
                "name": "Отеген Батыр",
                "uid": "26300f7d-161b-11ec-80d2-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "54",
            "attributes": {
                "name": "Восточно-Казахстанская область",
                "uid": "70181886-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "55",
            "attributes": {
                "name": "Алтай",
                "uid": "19c16d58-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "56",
            "attributes": {
                "name": "Зайсан",
                "uid": "265c4106-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "57",
            "attributes": {
                "name": "Риддер",
                "uid": "339bbb59-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "58",
            "attributes": {
                "name": "Семей",
                "uid": "339bbb5a-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "59",
            "attributes": {
                "name": "Усть-Каменогорск",
                "uid": "3fbc9e71-c772-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "60",
            "attributes": {
                "name": "Жамбылская область",
                "uid": "7c68b6f6-c71b-11ea-80bf-bc97e145c061",
                "shops": [
                    {
                        "id": 5,
                        "name": "Тараз Сатпаева",
                        "uid": "ddda4e0c-3a1a-11e3-a438-001e670c9280"
                    },
                    {
                        "id": 6,
                        "name": "Шу",
                        "uid": "9e1f51dc-03cc-11eb-80c2-bc97e145c062"
                    },
                    {
                        "id": 7,
                        "name": "Тараз Mall",
                        "uid": "faf9cf1d-0c3d-11eb-80c2-bc97e145c062"
                    },
                    {
                        "id": 8,
                        "name": "Сарыкемер",
                        "uid": "7bad3509-5a12-11eb-80c4-bc97e145c062"
                    },
                    {
                        "id": 9,
                        "name": "Тараз-Алатау",
                        "uid": "05c3421d-1151-11e8-80d6-1866da78d386"
                    }
                ]
            }
        },
        {
            "type": "City",
            "id": "61",
            "attributes": {
                "name": "Тараз",
                "uid": "2bc2cc06-c71c-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "62",
            "attributes": {
                "name": "Каратау",
                "uid": "3682bad0-c71c-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "63",
            "attributes": {
                "name": "Шу",
                "uid": "3682bad1-c71c-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "64",
            "attributes": {
                "name": "Кордай",
                "uid": "8800e08e-f252-11ea-80c0-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "65",
            "attributes": {
                "name": "Сарыкемер",
                "uid": "10c05dff-5a17-11eb-80c4-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "66",
            "attributes": {
                "name": "Западно-Казахстанская область",
                "uid": "858781e7-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "67",
            "attributes": {
                "name": "Аксай",
                "uid": "f00eadba-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "68",
            "attributes": {
                "name": "Уральск",
                "uid": "f00eadbb-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "69",
            "attributes": {
                "name": "Карагандинская область",
                "uid": "8cf26153-c71b-11ea-80bf-bc97e145c061",
                "shops": [
                    {
                        "id": 31,
                        "name": "Караганда",
                        "uid": "95f30e17-7d95-11e7-80d1-1866da78d386"
                    }
                ]
            }
        },
        {
            "type": "City",
            "id": "70",
            "attributes": {
                "name": "Караганда",
                "uid": "4744c9b9-c71c-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "71",
            "attributes": {
                "name": "Балхаш",
                "uid": "af8aac0a-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "72",
            "attributes": {
                "name": "Жезказган",
                "uid": "bc39c455-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "73",
            "attributes": {
                "name": "Сарань",
                "uid": "d2f22337-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "74",
            "attributes": {
                "name": "Сатпаев",
                "uid": "de4d2141-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "75",
            "attributes": {
                "name": "Шахтинск",
                "uid": "e58a2aab-c771-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "76",
            "attributes": {
                "name": "Темиртау",
                "uid": "2ab618c5-f252-11ea-80c0-bc97e145c062",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "77",
            "attributes": {
                "name": "Северо-Казахстанская область",
                "uid": "949f60b4-c71b-11ea-80bf-bc97e145c061",
                "shops": []
            }
        },
        {
            "type": "City",
            "id": "78",
            "attributes": {
                "name": "Петропавл",
                "uid": "dde2e103-c770-11ea-80bf-bc97e145c061",
                "shops": []
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 1,
            "count": 78
        }
    }
}
