from companies.models import Training, ContractType, Survey


def populate():

    for name in 'TRS Excel Maximising Mobility EES'.split(' '):
        training = Training()
        training.name = name
        training.save()

    for name in ['Forum Contract', 'Membership Contract', 'Local Contract', 'Free Participation', 'Local Membership']:
        contract_type = ContractType()
        contract_type.name = name
        contract_type.save()

    for name in ['TRS', 'Automotive', 'Financial Services', 'Mining', 'MLS', 'BPM']:
        survey = Survey()
        survey.name = name
        survey.save()

if __name__ == '__main__':
    populate()
