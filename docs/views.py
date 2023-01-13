from django.shortcuts import render
from rest_framework import viewsets, generics

from .serializers import EmployeesSerializer, PositionSerializer
from .models import Employees, Position
from .permissions import IsAuthenticated


class EmployeeRegisterView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    filterset_fields = ['fullname', ]
    ordering_fields = ['fullname', 'price']


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated, ]


class PositionViewSet(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filterset_fields = ['position', 'department']
    ordering_fields = ['position', 'department']


class PositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated, ]


