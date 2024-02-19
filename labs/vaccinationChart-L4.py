def insert(patient_record, record_num, first_name, last_name, birth_month):
    if record_num in patient_record:
        print(f"Record {record_num} already exists, Adding a new record is recomended.")
        return
    
    patient_record[record_num] = {
        'First Name': first_name,
        'Last Name': last_name,
        'Birth Months': birth_month
    }

patient_record = {}  # Initializing an empty dictionary to store the future patient data

# John Smith's updated vaccination details
john_smith = {
    'HepB': [0, 1, 6],
    'RV': [2, 4, 6],
    'DTaP': [2, 4, 6, 15],
    'Hib': [2, 4, 6, 12],
    'PCV13': [2, 4, 6, 12],
    'IPV': [2, 4, 6],
    'IIV4': 'Annual',
    'MMR': [12],
    'VAR': [12],
    'HepA': [12]
}

insert(patient_record, 'R001', 'John', 'Smith', john_smith)

# Olivia James's updated vaccination details
olivia_james = {
    'HepB': [0, 1, 6],
    'RV': [2, 4, 7],
    'DTaP': [2, 5, 7, 12],
    'Hib': [2, 4, 6, 12],
    'PCV13': [2, 5, 7, 12],
    'IPV': [2, 5, 8],
    'IIV4': 'Annual',
    'MMR': [12],
    'VAR': [12],
    'HepA': [12]
}

insert(patient_record, 'R002', 'Olivia', 'James', olivia_james)

print("Patient Dictionary: ")
for record, details in patient_record.items():
    print(record, details)

print("\nUpdated Patient Dictionary: ")
for record, details in patient_record.items():
    print(record, details)
