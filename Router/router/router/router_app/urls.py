from django.urls import path
from router.router_app.views import process_request

urlpatterns = [
    path('process_request/', process_request, name='process_request'),
]