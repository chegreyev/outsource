from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
# Create your views here.

class EmployeeViewSet(ModelViewSet):
    model = Employees
    queryset = model.objects.all()
    serializer_class = EmployeeSerializer

