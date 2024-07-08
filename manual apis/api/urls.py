from django.urls import path
from .views import departmentListAPI, departmentDetails, employeeListAPI, employeeDetailAPI

urlpatterns = [
    path("cmp/",departmentListAPI, name="departmentListAPI"),
    path("cmpdtl/<int:d_id>", departmentDetails, name="departmentDetails"),
    path("emp/",employeeListAPI, name="employeeListAPI"),
    path("empdtl/<int:e_id>", employeeDetailAPI, name="employeeDetailAPI"),
]