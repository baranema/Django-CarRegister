from rest_framework import generics
from rest_framework.response import Response
from .serializer import CarSerializer
from django.shortcuts import render
from .models import Car
from django.forms import ModelForm, ValidationError
from rest_framework.views import APIView
from .forms import CarForm
from django.shortcuts import redirect
from re import match

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

class CarEdit(APIView):
    def post(self, request, pk):
        form = CarForm(request.POST or None, instance=Car.objects.get(pk=pk))

        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('all_entries')
        else:  
            carPlate = Car.objects.get(pk=pk).carPlate

            if not match(Car.PLATE_REGEX, carPlate): 
                regex_error = ValidationError("The car plate number does not match any approved plate number examples.")
 
            return render(request=request, template_name="entry.html", context={'form': form, 'error': regex_error})

    def get(self, request, pk):
        carForm = CarForm(instance=Car.objects.get(pk=pk))
        return render(request=request, template_name="entry.html", context={'form': carForm})


class CarCreate(APIView): 
    def post(self, request):
        form = CarForm(request.POST) 

        if form.is_valid():
            carPost = form.save()
            carPost.save()
            return redirect('all_entries')
        else:
            return render(request=request, template_name="entry.html", context={'form': form, 'error': form.errors})

    def get(self, request):
        form = CarForm()
        return render(request=request, template_name="entry.html", context={'form': form})


class CarList(APIView): 
    def get(self, request):
        cars = Car.objects.all() 

        if cars:
            return render(None, 'all_entries.html', {'cars': cars})
        else:
            return render(request=request, template_name='all_entries.html')