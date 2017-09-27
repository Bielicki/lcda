from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=64)
    client = models.ForeignKey(Client, related_name='companies')
    code = models.CharField(max_length=32)
    engagement_specialist = models.EmailField()
    #super_sector = models.ForeignKey('SuperSector')
    contract_type = models.ForeignKey('ContractType', related_name='years')
    super_sector = models.CharField(max_length=32)
    surveys = models.ManyToManyField('Survey', related_name='companies')
    grading = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    general_comments = models.TextField()

    def __str__(self):
        return self.name


class SuperSector(models.Model):
    name = models.CharField(max_length=32)
    sector = models.ForeignKey('Sector', related_name='supersector')

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=32)
    subsector = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Survey(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class YearOfParticipation(models.Model):
    year = models.PositiveIntegerField()
    surveys = models.ManyToManyField(Survey, related_name='years')
    company = models.ForeignKey('Company', related_name='years')
    active = models.BooleanField()
    client_contacts = models.ManyToManyField('ClientContact')

    def __str__(self):
        return str(self.year)


class ContractType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class ClientContact(models.Model):
    designation = models.CharField(max_length=8)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    company = models.ForeignKey(Company, related_name='contacts')
    business_phone = models.CharField(max_length=32)
    mobile = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    comment = models.TextField()
    notes = models.TextField()
    may_contact = models.BooleanField()
    surveys = models.ManyToManyField(Survey, related_name='clients')
    launch_meeting = models.BooleanField()
    after_meeting = models.BooleanField()
    trainings = models.ManyToManyField('Training', related_name='contacts')
    access = models.BooleanField()
    report_access = models.BooleanField()
    invoice = models.BooleanField()

    def __str__(self):
        return f'{self.designation} {self.first_name} {self.last_name}'


class Training(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
