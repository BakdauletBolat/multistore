
from handbook.models.Category import Category
from rest_framework.exceptions import NotFound


class GetCategory:

    def __init__(self,id,store_id,is_raise_return=True) -> None:
        self.id = id
        self.store_id = store_id
        self.is_raise_return = is_raise_return

    def run(self):
        try:
            category = Category.objects.get(id=self.id,store_id=self.store_id)
            return category
        except Category.DoesNotExist:
            if self.is_raise_return:
                raise NotFound(detail='Category does not exist')
            else:
                return NotFound(detail='Category does not exist') 
