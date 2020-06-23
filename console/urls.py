from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('versions', views.version_list, name='version_list'),
]
