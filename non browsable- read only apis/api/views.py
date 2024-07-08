from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class companyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # url =  companies/{company_id}/employees 
    @action(detail=True, methods=["get"])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(Company = company)
            emps_serializer = EmployeeSerializer(emps, many=True, context = {"request":request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                "message": f"{e}"  # "company doesn't exists."
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer




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
    # print("home page requested")
    friends = {
        "friend 1":"imroz khan", 
        "friend 2":"aman hasan",
        "friend 3":"faisal khan"
    }
    return JsonResponse(friends, safe=False)
