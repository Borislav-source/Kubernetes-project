from django.urls import path
from worker1.app.views import my_view

urlpatterns = [
    path('my-endpoint/', my_view, name='my_view'),
]