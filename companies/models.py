from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Company(models.Model):
    client = models.ForeignKey(Client, related_name='companies')
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    #   Sectors TO BE IMPLEMENTED
    grading_system = models.CharField(max_length=32)  # Choice in the Future
    address = models.CharField(max_length=128)
    general_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class YearOfParticipation(models.Model):
    year = models.PositiveIntegerField()
    company = models.ForeignKey('Company', related_name='years')
    company_setup = models.ForeignKey('CompanySetup', related_name='year')

    def __str__(self):
        return str(self.year)


class CompanySetup(models.Model):
    engagement_specialist = models.EmailField()
    contract_type = models.CharField(max_length=32)  # Choice in the Future
    is_active = models.BooleanField()
    surveys = models.CharField(max_length=32)  # Choice in the Future

    def __str__(self):
        return f'Company Setup {self.id}'


class ClientContact(models.Model):
    company = models.ForeignKey(Company, related_name='contacts')
    designation = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    business_phone = models.CharField(max_length=32)
    mobile = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    comment = models.TextField()
    notes = models.TextField()
    may_contact = models.BooleanField()

    def __str__(self):
        return f'{self.designation} {self.first_name} {self.last_name}'


class ContactSetup(models.Model):
    year = models.ForeignKey(YearOfParticipation, related_name='contacts')
    client_contact = models.ForeignKey(ClientContact, related_name='setups')
    surveys = models.CharField(max_length=32)  # Choice in the Future
    launch_meeting = models.BooleanField()
    after_meeting = models.BooleanField()
    trainings = models.CharField(max_length=32)  # Choice in the Future
    access = models.BooleanField()
    report_access = models.BooleanField()
    invoice = models.BooleanField()

    def __str__(self):
        return f'{self.client_contact} - {self.year}'
