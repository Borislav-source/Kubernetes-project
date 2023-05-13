from django.urls import path
from worker2.fibonacci.views import fibonacci_resolver

urlpatterns = [
    path('resolve/', fibonacci_resolver, name='fibonacci_resolver'),
]
