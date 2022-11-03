from handbook.models import Category
from rest_framework.exceptions import NotFound


class GetCategory:

    def __init__(self, id, store_id, is_raise_return=True) -> None:
        self.id = id
        self.store_id = store_id
        self.is_raise_return = is_raise_return

    def run(self):
        try:
            category = Category.objects.get(id=self.id, stores__in=[self.store_id])
            return category
        except Category.DoesNotExist:
            if self.is_raise_return:
                raise NotFound(detail='Category does not exist')
            else:
                return NotFound(detail='Category does not exist')


class GetRecurciveCategoryIdsByParent:

    def __init__(self, main_category, store_id) -> None:
        self.main_category = main_category
        self.store_id = store_id
        self.ids = set()

    def get_all_category_ids(self, main_category):
        self.ids.add(main_category.id)
        for category in main_category.categories.filter(stores__in=[self.store_id]):
            for c in main_category.categories.filter(stores__in=[self.store_id]):
                self.ids.add(c.id)
            if len(category.categories.filter(stores__in=[self.store_id])) <= 0:
                return 1
            else:
                self.get_all_category_ids(category)

    def run(self):
        self.get_all_category_ids(self.main_category)
        return list(self.ids)
