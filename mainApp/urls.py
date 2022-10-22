from django.urls import path, include
from . import views

urlpatterns = [

       # path('', include('mainApp.urls')),
        path('', views.index, name='index'),
]
