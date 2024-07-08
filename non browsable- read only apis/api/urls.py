from django.urls import path, include
from .views import companyViewSet, home, EmployeeViewSet 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"companies", companyViewSet)
router.register(r"employee", EmployeeViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("home", home, name="home"),
]
