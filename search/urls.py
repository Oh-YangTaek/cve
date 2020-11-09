from django.urls import path
from search import views

urlpatterns =[
    path('',views.Main),
    path('list', views.ListFunc),
]
