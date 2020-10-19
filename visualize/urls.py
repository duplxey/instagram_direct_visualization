from django.urls import path

from visualize import views

urlpatterns = [
    path("", views.index_view, name='visualize-index'),
    path("get/", views.get_view, name='visualize-get'),
]