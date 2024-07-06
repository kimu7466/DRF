from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

from rest_framework import viewsets


class companyViewSet(viewsets.ModelViewSet):
    pass































# def home(request):
#     print("home page requested")
#     return HttpResponse("<h1> this is home page </h1>")


# def home(request):
    # print("home page requested")
    # friends = [
    #     "imroz khan", 
    #     "aman hasan",
    #     "faisal khan"
    # ]
    # return JsonResponse(friends, safe=False)

def home(request):
    print("home page requested")
    friends = {
        "friend 1":"imroz khan", 
        "friend 2":"aman hasan",
        "friend 3":"faisal khan"
    }
    return JsonResponse(friends, safe=False)
