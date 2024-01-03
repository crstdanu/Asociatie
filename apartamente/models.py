from django.db import models

# Create your models here.

WATER_PRICE = 5
SERVICE_PRICE = 3


class Apartament(models.Model):
    apartment_number = models.PositiveIntegerField()
    owner_first_name = models.CharField(max_length=50)
    owner_last_name = models.CharField(max_length=50)
    inhabitants_nr = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    # TODO - change to cold_water_consumption
    cold_water_index = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Apartment {self.apartment_number}. Owner: {self.owner_first_name} {self.owner_last_name}'

    def calculate_total_costs(self):
        total = self.calculate_water_price() + self.calculate_service_cost()
        return float(total)

    def calculate_service_cost(self):
        return (self.inhabitants_nr * SERVICE_PRICE)

    def calculate_water_price(self):
        return (self.cold_water_index * WATER_PRICE)
