from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import CarForm
from .models import Car

class MainPage(ListView):
    template_name='CarApp/home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.all() 

def carview(request):
    if request.method == 'POST': 
        carform = CarForm(request.POST, request.FILES) 
    if carform.is_valid(): 
        carform.save() 
    return redirect('home') 
  
    carform = CarForm()
    return render(request,'CarApp/add.html', {'form': carform})
   
def update(request, pk, template_name='CarApp/update.html'):
    car= get_object_or_404(Car, pk=pk) 

    form = CarForm(request.POST or None, request.FILES or None, instance=car )
    
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})
 
def remove(request, pk, template_name='CarApp/remove.html'):
    car= get_object_or_404(Car, pk=pk)     
    if request.method=='POST':
        car.delete()
        return redirect('home')
    return render(request, template_name, {'object':car})