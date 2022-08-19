from django.urls import path,include
from handbook.ui.api.controllers.samsung.GetTreeCategories import GetTreeCategories

urlpatterns_handbook = [
    path('handbook/',include([
        path('samsung/',include([
            path('tree-categories/',GetTreeCategories.as_view())
        ]))
    ]))
]