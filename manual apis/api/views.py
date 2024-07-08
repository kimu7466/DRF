from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render

from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer
# Create your views here.

@api_view(['GET',"POST"])
def departmentListAPI(request):
    if request.method == "GET":
        queryset = Departments.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","PATCH","DELETE"])
def departmentDetails(request, d_id):
    try :
        queryset = Departments.objects.get(id = d_id)
    except Exception as e:
        return Response({"message":"Department not found"}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = DepartmentSerializer(queryset)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = DepartmentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = DepartmentSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET',"POST"])
def employeeListAPI(request):
    if request.method == "GET":
        queryset = Employees.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def employeeDetailAPI(request, e_id):
    try :
        queryset = Employees.objects.get(id=e_id)
    except Exception as e:
        return Response({"message":f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = EmployeeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = EmployeeSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = EmployeeSerializer(queryset, data=request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
    
    return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
