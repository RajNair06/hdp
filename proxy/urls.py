from django.urls import path
from .views import Catch

urlpatterns=[
    path('catch/',Catch.as_view()),

]