from django.contrib import admin
from .models import Company, Client, YearOfParticipation, ClientContact, CompanySetup, ContactSetup


@admin.register(Company, Client, YearOfParticipation, ClientContact, CompanySetup, ContactSetup)
class Admin(admin.ModelAdmin):
    pass
