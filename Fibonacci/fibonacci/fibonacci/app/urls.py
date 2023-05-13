from django.urls import path
from fibonacci.app.views import fibonacci_resolver


urlpatterns = [
    path('resolve/', fibonacci_resolver, name='fibonacci_resolver'),
]