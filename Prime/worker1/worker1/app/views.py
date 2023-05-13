from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError


def my_view(request):
    num = request.GET.get('num')
    if num:
        num = int(num)
        x = None
        for i in range(2, num):
            if num % i == 0:
                x = i
        if not x:
            return HttpResponse('''status code - 200 OK'
                                '{"result": "prime "}''')
        return HttpResponseServerError('status code - 500 {"result": "not-prime", "description": 'f"{num} is "
                                       f"divisible by {x}"'}.')
    else:
        return HttpResponse("Please provide a 'num' parameter in the URL")
