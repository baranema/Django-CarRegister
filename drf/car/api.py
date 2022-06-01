from rest_framework import generics
from rest_framework.response import Response
from .serializer import CarSerializer
from django.shortcuts import render
from .models import Car
from rest_framework.views import APIView

class CarCreateApi(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarApi(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDeleteApi(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarList(APIView):
    def get(self, request):
        queryset = Car.objects.all()
        if queryset:
            response = render(None, 'all_entries.html', {'cars': queryset})
        else:
            response = render(request=request, template_name='all_entries.html')

        return response