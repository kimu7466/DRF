from django.db import models

# Create your models here.


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Departments(BaseClass):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} -- {self.name}"
    
class Employees(BaseClass):
    id = models.AutoField(primary_key=1)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.IntegerField()
    dep_id = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} -- {self.name} -- {self.dep_id}"
