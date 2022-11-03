from django.urls import path, include
from handbook.views.api import GetTreeCategoriesView
from handbook.views.admin import CategoryListView, CitiesListByStoreView

urlpatterns = [
    path('samsung/', include([
        path('tree-categories/', GetTreeCategoriesView.as_view())
    ])),
    path('admin/', include([
        path('categories/', CategoryListView.as_view()),
        path('cities/', CitiesListByStoreView.as_view())
    ]))
]
