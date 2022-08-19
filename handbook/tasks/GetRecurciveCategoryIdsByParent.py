class GetRecurciveCategoryIdsByParent:

    def __init__(self,main_category,store_id) -> None:
        self.main_category = main_category
        self.store_id = store_id
        self.ids = set()

    
    def get_all_category_ids(self,main_category):
            self.ids.add(main_category.id)
            for category in main_category.categories.filter(store_id=self.store_id):
                for c in main_category.categories.filter(store_id=self.store_id):
                    self.ids.add(c.id)
                if len(category.categories.filter(store_id=self.store_id)) <= 0:
                    return 1
                else:
                    self.get_all_category_ids(category)

    def run(self):
        self.get_all_category_ids(self.main_category)
        return list(self.ids)