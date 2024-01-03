from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Apartament
from .forms import ApartmentForm


# Create your views here.
def index(request):
    return render(request, 'apartamente/index.html', {
        'apartamente': Apartament.objects.all()
    })


def view_apartment(request, id):
    apartment = Apartament.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            new_apartment_number = form.cleaned_data['apartment_number']
            new_owner_first_name = form.cleaned_data['owner_first_name']
            new_owner_last_name = form.cleaned_data['owner_last_name']
            new_inhabitants_nr = form.cleaned_data['inhabitants_nr']
            new_email = form.cleaned_data['email']
            new_address = form.cleaned_data['address']
            new_cold_water_index = form.cleaned_data['cold_water_index']

            new_apartament = Apartament(
                apartment_number=new_apartment_number,
                owner_first_name=new_owner_first_name,
                owner_last_name=new_owner_last_name,
                inhabitants_nr=new_inhabitants_nr,
                email=new_email,
                address=new_address,
                cold_water_index=new_cold_water_index
            )
            new_apartament.save()
            return render(request, 'apartamente/add.html', {
                'form': ApartmentForm(),
                'success': True
            })
    else:
        form = ApartmentForm()
    return render(request, 'apartamente/add.html', {
        'form': ApartmentForm()
    })


def edit(request, id):
    if request.method == 'POST':
        apartment = Apartament.objects.get(pk=id)
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            return render(request, 'apartamente/edit.html', {
                'form': form,
                'success': True
            })
    else:
        apartment = Apartament.objects.get(pk=id)
        form = ApartmentForm(instance=apartment)
    return render(request, 'apartamente/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        apartment = Apartament.objects.get(pk=id)
        apartment.delete()
    return HttpResponseRedirect(reverse('index'))


def view(request, id):
    return render(request, 'apartamente/view.html', {
        'apartamente': Apartament.objects.get(pk=id)
    })
