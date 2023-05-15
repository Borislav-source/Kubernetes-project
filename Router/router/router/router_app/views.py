from django.shortcuts import render
from django.http import HttpResponse
import requests, random

a = 0


def process_request(request):
    # Get the request parameters
    #num = request.GET.get('num')
    request_params = request.GET
    global a
    
    # Send the request to the stateless service
    #service_name = "worker1" if random.choice([True, False]) else "worker2"
    if a < 10:
        a += 1
        response = requests.get(f"http://worker1-cluster-ip-service:8000/app/my-endpoint/", params=request_params)
    else:
        a = 0
        response = requests.get(f"http://worker2-cluster-ip-service:8000/resolve/", params=request_params)
    # Return the response from the stateless service
    return HttpResponse(response.text)