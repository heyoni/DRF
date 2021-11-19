from django.urls import path,include
from .views import helloAPI, randomQuizAPI

urlpatterns=[
    path('hello/',helloAPI),
    path('<int:id>/',randomQuizAPI)
]