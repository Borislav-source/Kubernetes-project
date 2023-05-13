from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
import itertools


# Create your views here.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_resolver(request):
    num = request.GET.get('num')
    if num:
        num = int(num)
        fibonacci_numbers = list(itertools.islice(fibonacci(), 50))
        if num in fibonacci_numbers:
            return HttpResponse('status code - 200 OK {"result": "exists"}')
        return HttpResponseServerError('status code - 500 {"result": "does-not-exists"}')
    return HttpResponse('Please provide a number')