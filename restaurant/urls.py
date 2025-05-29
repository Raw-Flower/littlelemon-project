from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView

urlpatterns = [
    path(route='',view=index,name='home'),
    path(route='menu/', view=MenuItemView.as_view()),
    path(route='menu/<int:pk>', view=SingleMenuItemView.as_view()),
]
