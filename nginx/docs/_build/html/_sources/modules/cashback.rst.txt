Кэшбек(Стандарт)
***********************************

API для создания кэшбек акции

:mod:`Сделайте запрос методом POST по ссылке: /api/v1/sale/cashbacktype/create/ для создания акции "Кэшбек"`
:mod:`Сделайте запрос методом POST по ссылке: /api/v1/sale/standarttype/create/ для создания акции "Стандарт"`

*Headers*::

    - header 'Authorization: {Token}'
    - header 'Content-Type: application/json'
    

*Тело запроса*:

.. code-block:: json
    
    {
        "data": {
            "type": "Sale",
            "attributes": {
                "accural_percent": 5,
                "writeoff_percent": 80,
                "activate_at": 20,
                "sale_type": "cashbacktype",
                "prioritet": 7,
                "products_ids": [40],
                "start_date": "2022-07-05 11:30:00",
                "end_date":  "2022-10-05 11:30:00",
                "payment_method_ids": [1],
                "cities_ids": [1],
                "shops_ids": [1, 2, 3],
                "is_intersects_sales_ids": [],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_reverse": false,
                "is_compensated": true
        
            }
        }   
        
    }

.. function:: post
   
   - Обязательные поля:

   :param type: Тип используемой модели
   :type type: str
   :param accural_percent: Процент начисления бонусов
   :type accural_percent: int
   :param writeoff_percent: Процент возможного списания за раз бонусов
   :type writeoff_percent: int
   :param activate_at: Количество дней через которые активируются бонусы
   :type activate_at:  int
   :param sale_type: Поле, которое указывает тип акции
   :type sale_type: str
   :param prioritet: Поле, которые указывает приоритетность акции
   :type prioritet: int
   :param products_ids: Поле, которое указывает список id продуктов
   :type products_ids: int array
   :param start_date: Дата начала акции
   :type start_date: datetime
   :param end_date: Дата конец акции
   :type end_date: datetime
   :param payment_method_ids: Список id разрешенных способов оплаты
   :type payment_method_ids: int array
   :param cities_ids: Список id разрешенных городов
   :type cities_ids: int array
   :param shops_ids: Список id разрешенных магазинов
   :type shops_ids: int array
   :param is_intersects_sales_ids: Список разрешенных пересекаемых акций
   :type is_intersects_sales_ids: int array
   
   - Необязательные поля:

   :type is_intersects_sales_ids: int array
   :param is_use_of_bonuses: Разрешение на использование бонусов совместно с акцией
   :type is_use_of_bonuses: bool
   :param is_manual_sale: Параметр определяющий это ручная скидка
   :type is_manual_sale:   bool
   :param is_accrual_bonuses: "Boolean", начисляется или нет
   :param is_reverse: Параметр при котором определяется поле "products" это список разрешенных или исключенные товары
   :type is_reverse: bool
   :param is_compensated: Параметр определяющий разрешение компенсации
   :type is_compensated: bool

*Ответ*::

    - Status: 201 Created

*Тело ответа*:

.. code-block:: json

    {
        "data": {
            "type": "Sale",
            "id": "60",
            "attributes": {
                "start_date": "2022-07-05T11:30:00+06:00",
                "end_date": "2022-10-05T11:30:00+06:00",
                "payment_method": [
                    {
                        "id": 1,
                        "name": "Наличные",
                        "is_active": true
                    }
                ],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 7,
                "sale_type": "cashbacktype",
                "is_active": true,
                "author_id": 1
            },
            "relationships": {
                "is_intersects_sales": {
                    "data": []
                },
                "content_object": {
                    "data": {
                        "accural_percent": 5,
                        "writeoff_percent": 80,
                        "activate_at": 20
                    }
                }
            }
        }
    }
