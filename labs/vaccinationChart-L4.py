def insert(patient_record, record_num, first_name, last_name, vaccine_data):
    if record_num in patient_record: #Checks if new record number is in the record directory
        print(f"Record {record_num} already exists.")
        return

    patient_record[record_num] = {
        'First Name': first_name,
        'Last Name': last_name,
        'Vaccines': vaccine_data
    }

def process_vaccine_data(vaccine_list):
    vaccine_data = {}
    for vaccine in vaccine_list:
        vaccine_name, months = vaccine[0], vaccine[1]
        if months != 'Annual':
            vaccine_data[vaccine_name] = [int(month) for month in months]
        else:
            vaccine_data[vaccine_name] = months
    return vaccine_data

patient_record = {}

# John Smith's vaccine data
john_smith_vaccines = [
    ('HepB', '016'),
    ('RV', '246'),
    ('DTaP', '24615'),
    ('Hib', '24612'),
    ('PCV13', '24612'),
    ('IPV', '246'),
    ('IIV4', 'Annual'),
    ('MMR', '12'),
    ('VAR', '12'),
    ('HepA', '12')
]
john_smith_data = process_vaccine_data(john_smith_vaccines)
insert(patient_record, 'R001', 'John', 'Smith', john_smith_data)

# Olivia James's vaccine data
olivia_james_vaccines = [
    ('HepB', '016'),
    ('RV', '247'),
    ('DTaP', '25712'),
    ('Hib', '24612'),
    ('PCV13', '25712'),
    ('IPV', '258'),
    ('IIV4', 'Annual'),
    ('MMR', '12'),
    ('VAR', '12'),
    ('HepA', '12')
]
olivia_james_data = process_vaccine_data(olivia_james_vaccines)
insert(patient_record, 'R002', 'Olivia', 'James', olivia_james_data)

# Printing the patient dictionary
print("Patient Dictionary: ")
for record, details in patient_record.items():
    print(record, details)
