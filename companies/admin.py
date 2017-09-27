from django.contrib import admin
from .models import Company, Client, Survey, SuperSector, Sector, Training, ContractType, ClientContact


@admin.register(Company, Client, Survey, SuperSector, Sector, Training, ContractType, ClientContact)
class Admin(admin.ModelAdmin):
    pass