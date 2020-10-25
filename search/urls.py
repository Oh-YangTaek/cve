from django.urls import path
from search import views

urlpatterns =[
    path('',views.Main),
    path('list', views.ListFunc),
    path('test', views.test),
    path('test2',views.test2),
]
