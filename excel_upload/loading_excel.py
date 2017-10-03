import pandas as pd

from companies.models import Company, Client, ClientContact, YearOfParticipation, ContactSetup, CompanySetup

# TODO:
# - Populate Static Models
# - Change Yes/No to True/False


def boolify(string):
    if string == 'yes':
        return True
    elif string.lower() == 'no':
        return False


def load_excel(file):
    df = pd.read_excel(file, header=None)

    column_names = df.iloc[2]
    df = df.iloc[3:]
    df.columns = column_names

    unique_clients = df['South Africa CLIENT DATABASE'].unique()

    for client_name in unique_clients:

        if not Client.objects.filter(name=client_name):
            Client(name=client_name).save()

        # Unique Companies for a Client
        unique_companies = df[df['South Africa CLIENT DATABASE'] == client_name]['Local Company name'].unique()
        for company_name in unique_companies:

            company_data = df[df['Local Company name'] == company_name]

            if not Company.objects.filter(name=company_name):
                company = Company()
                company.client_id = Client.objects.get(name=client_name).id
                company.name = company_name
                company.code = company_data['The CODE'].iloc[0]
                # company.super_sector = company_data['Super Sector'].iloc[0]
                company.grading = company_data['Grading System'].iloc[0]
                company.address = company_data['Company Physical Address'].iloc[0]
                company.general_comments = company_data['General Comments'].iloc[0]
                company.save()

            else:
                company = Company.objects.get(name=company_name)

            company_setup = CompanySetup()
            company_setup.engagement_specialist = company_data['Engagement Specialist'].iloc[0]
            company_setup.contract_type = company_data['Contract type'].iloc[0]
            company_setup.is_active = True
            company_setup.surveys = company_data['2017 Surveys'].iloc[0]
            company_setup.save()

            contacts = company_data['E-mail address'].unique()
            for contact in contacts:

                if not ClientContact.objects.filter(email=contact):
                    client_contact = ClientContact()
                    client_contact.company_id = company.id
                    client_contact.designation = company_data['Designation'].iloc[0]
                    client_contact.first_name = company_data['Name'].iloc[0]
                    client_contact.last_name = company_data['Surname'].iloc[0]
                    client_contact.email = company_data['E-mail address'].iloc[0]
                    client_contact.business_phone = company_data['Business Phone +27'].iloc[0]
                    client_contact.mobile = company_data['Mobile/Cell +260'].iloc[0]
                    client_contact.location = company_data['Location'].iloc[0]
                    client_contact.comment = company_data['Comments'].iloc[0]
                    client_contact.notes = company_data['Notes (CST)'].iloc[0]
                    client_contact.may_contact = company_data['May contact?'].apply(boolify).iloc[0]
                    client_contact.save()

                else:
                    client_contact = ClientContact.objects.get(email=contact)

                if not YearOfParticipation.objects.filter(year=2017, company_id=company.id):
                    year = YearOfParticipation(year=2017, company_id=company.id, company_setup=company_setup)
                    year.save()
                else:
                    year = YearOfParticipation.objects.get(year=2017, company_id=company.id)

                if not ContactSetup.objects.filter(client_contact_id=client_contact.id, year_id=year.id):
                    contact_setup = ContactSetup()
                    contact_setup.year_id = year.id
                    contact_setup.client_contact_id = client_contact.id
                    contact_setup.launch_meeting = True
                    contact_setup.after_meeting = True
                    contact_setup.access = True
                    contact_setup.report_access = True
                    contact_setup.invoice = True
                    contact_setup.trainings = 'TRS Automotive'
                    contact_setup.save()

    return None
