def insert(patient_record, record_num, first_name, last_name, vaccine_info):
    # Check record number's existance
    if record_num in patient_record:
        print(f"Record {record_num} already exists.")
        return

    # Insert new data
    patient_record[record_num] = {
        'First Name': first_name,
        'Last Name': last_name,
        'Vaccines': vaccine_info
    }

def vaccine_info(vaccine_list):
    vaccine_info = {}
    # Convert vaccine schedule to the required format
    for vaccine in vaccine_list:
        vaccine_name, months = vaccine[0], vaccine[1]
        #Convert to integers other than annual vaccines
        if months != 'Annual':
            vaccine_info[vaccine_name] = [int(month) for month in months.split()]
        else:
            vaccine_info[vaccine_name] = months
    return vaccine_info
#Record dictionary 
patient_record = {}

#John's data given
john_smith = [
    ('HepB', '016'), ('RV', '2 4 6'), ('DTaP', '2 4 6 15'), ('Hib', '2 4 6 12'), ('PCV13', '2 4 6 12'), ('IPV', '2 4 6'), ('IIV4', 'Annual'), ('MMR', '12'), ('VAR', '12'), ('HepA', '12')
]
#Calling function to process John's info
new_john_smith = vaccine_info(john_smith)
insert(patient_record, 'R001', 'John', 'Smith', new_john_smith)

#Olivia's data given 
olivia_james = [
    ('HepB', '016'), ('RV', '2 4 7'), ('DTaP', '2 5 7 12'), ('Hib', '2 4 6 12'), ('PCV13', '2 5 7 12'), ('IPV', '2 5 8'), ('IIV4', 'Annual'), ('MMR', '12'), ('VAR', '12'), ('HepA', '12')
]
#Calling function to process Olivia's info 
new_olivia_james = vaccine_info(olivia_james)
insert(patient_record, 'R002', 'Olivia', 'James', new_olivia_james)

#Displays patient dictionary
print("Patient Dictionary: ")
for record, details in patient_record.items():
    print(record, details)
