import pandas as pd

from companies.models import Company, Client, ClientContact, SuperSector, Sector, Survey, Training, ContractType, YearOfParticipation

# TODO:
# - Populate Static Models
# - Change Yes/No to True/False


def boolify(string):
    if string == 'yes':
        return True
    elif string.lower() == 'no':
        return False


def pay_boolify(string):
    if string.lower() == 'paid':
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
        if not Client.objects.filter(name=client_name).exists():
            print('creating client')
            client = Client(name=client_name).save()
        else:
            client = Client.objects.get(name=client_name)

        unique_companies = df[df['South Africa CLIENT DATABASE'] == client_name]['Local Company name'].unique()

        for company_name in unique_companies:
            company_data = df[df['Local Company name'] == company_name]
            if not Company.objects.filter(name=company_name):
                company = Company()

                company.name = company_name
                company.engagement_specialist = company_data['Engagement Specialist'].iloc[0]
                company.client_id = Client.objects.get(name=client_name).id
                company.code = company_data['The CODE'].iloc[0]
                company.super_sector = company_data['Super Sector'].iloc[0]
                company.grading = company_data['Grading System'].iloc[0]
                company.address = company_data['Company Physical Address'].iloc[0]
                company.general_comments = company_data['General Comments'].iloc[0]
                company.contract_type = ContractType.objects.get(name=company_data['Contract type'].iloc[0])
                company.save()

                try:
                    s = ['TRS', 'Automotive', 'Financial Services', 'Mining', 'MLS', 'BPM']
                    surveys = [Survey.objects.get(name=survey) for survey in s if survey in company_data['2017 Surveys'].iloc[0]]
                    company.surveys.add(*surveys)
                    company.save()
                except TypeError:
                    pass

            else:
                company = Company.objects.get(name=company_name)

            year = YearOfParticipation()
            year.year = 2017

            year.company = company


            year.active = True
            year.save()

            contacts = company_data['E-mail address'].unique()
            contact_list = []

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
                    client_contact.launch_meeting = company_data['2017 Launch Mtg'].apply(boolify).iloc[0]
                    client_contact.after_meeting = True
                    client_contact.access = True
                    client_contact.report_access = True
                    client_contact.invoice = True
                    client_contact.save()

                    try:
                        s = ['TRS', 'Automotive', 'Financial Services', 'Mining', 'MLS', 'BPM']
                        surveys = [Survey.objects.get(name=survey) for survey in s if survey in company_data['2017 Surveys'].iloc[0]]
                        client_contact.surveys.add(*surveys)
                    except TypeError:
                        pass

                    trainings = [Training.objects.get(name=training) for training in 'TRS Excel Maximising Mobility EES'.split(' ')]
                    client_contact.trainings.add(*trainings)
                    client_contact.save()
                else:
                    client_contact = ClientContact.objects.get(email=contact)

                contact_list.append(client_contact)

            year.client_contacts.add(*contact_list)

    return None
