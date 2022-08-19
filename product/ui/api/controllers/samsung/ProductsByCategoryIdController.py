from rest_framework.generics import ListAPIView
from handbook.tasks.GetCategory import GetCategory
from handbook.tasks.GetRecurciveCategoryIdsByParent import GetRecurciveCategoryIdsByParent 
from product.models.Product import Product
from product.tasks.GetProductsByCategoryIds import GetProductsByCategoryIds
from product.ui.api.transformers.ProductTransformer import ProductTransformer
from multistore.config.pagination import StandartResultsSetPagination
from rest_framework.exceptions import ValidationError


class ProductsByCategoryIdController(ListAPIView):

    serializer_class = ProductTransformer
    queryset = Product.objects.all()
    pagination_class = StandartResultsSetPagination

    def get_queryset(self,*args, **kwargs):
        category_id = self.kwargs.get('category_id',None)

        if category_id is None:
            raise ValidationError(detail='category_id not specified')
        
        main_category = GetCategory(id=category_id,store_id=1).run()

        ids = GetRecurciveCategoryIdsByParent(main_category=main_category,store_id=1).run()
        products = GetProductsByCategoryIds(ids=ids).run()

        return products
