from django import forms
from .models import Apartament
from django.core.exceptions import ValidationError


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartament
        fields = ['apartment_number', 'owner_first_name', 'owner_last_name',
                  'inhabitants_nr', 'email', 'address', 'cold_water_index']
        labels = {
            'apartment_number': 'Apartment number',
            'owner_first_name': "Owner's First Name",
            'owner_last_name': "Owner's Last Name",
            'inhabitants_nr': 'Number of inhabitants',
            'email': "Owner's email address",
            'address': "Address",
            'cold_water_index': 'Current Cold Water Index'
        }
        # a widget is Django's representation of an HTML input element
        # the widget handles the rendering of the html and the extraction of data from a GET or POST dictionary that coresponds to the widget
        widgets = {
            'apartment_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'owner_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'inhabitants_nr': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'cold_water_index': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        apartment_number = cleaned_data.get('apartment_number')
        address = cleaned_data.get('address')

        queryset = Apartament.objects.exclude(pk=self.instance.pk)
        if queryset.filter(apartment_number=apartment_number, address=address).exists():
            raise ValidationError(
                "Apartment with the same number and address already exists.")

        return cleaned_data
