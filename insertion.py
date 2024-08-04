import mysql.connector

# Establishing connection to MySQL database
db_connection = mysql.connector.connect(
            host="localhost",
            user="hari",
            password="hari4114",
            database="HospitalManagementSystem"
)

# Creating a cursor object
cursor = db_connection.cursor()

# Inserting data into donorbank table
donorbank_data = [
    (1, 'Red Cross Blood Bank'),
    (2, 'LifeLine Blood Bank'),
    (3, 'Hope Blood Bank'),
    (4, 'Angel Blood Bank'),
    (5, 'Unity Blood Bank'),
    (6, 'Care Blood Bank'),
    (7, 'Sunshine Blood Bank'),
    (8, 'Grace Blood Bank'),
    (9, 'Harmony Blood Bank'),
    (10, 'Samaritan Blood Bank')
]

donorbank_insert_query = "INSERT INTO donorbank (DonorBankID, Name) VALUES (%s, %s)"
cursor.executemany(donorbank_insert_query, donorbank_data)

# Inserting data into donor table
donor_data = [
    (1, 'Rajesh Sharma', 1),
    (2, 'Priya Patel', 2),
    (3, 'Amit Singh', 3),
    (4, 'Reena Gupta', 4),
    (5, 'Rahul Kumar', 5),
    (6, 'Neha Sharma', 6),
    (7, 'Ankit Verma', 7),
    (8, 'Sonia Jain', 8),
    (9, 'Vivek Gupta', 9),
    (10, 'Meera Singh', 10)
]

donor_insert_query = "INSERT INTO donor (DonorID, DonorName, DonorBankID) VALUES (%s, %s, %s)"
cursor.executemany(donor_insert_query, donor_data)

# Inserting data into blooddonor table
blooddonor_data = [
    (1, 'A+'),
    (2, 'B-'),
    (3, 'O+'),
    (4, 'AB+'),
    (5, 'A-'),
    (6, 'O-'),
    (7, 'B+'),
    (8, 'AB-'),
    (9, 'A+'),
    (10, 'O-')
]

blooddonor_insert_query = "INSERT INTO blooddonor (DonorID, BloodType) VALUES (%s, %s)"
cursor.executemany(blooddonor_insert_query, blooddonor_data)

# Inserting data into marrowdonor table
marrowdonor_data = [
    (1, 'Stem cells'),
    (2, 'Bone marrow'),
    (3, 'Peripheral blood stem cells'),
    (4, 'Cord blood'),
    (5, 'Granulocyte-colony stimulating factor'),
    (6, 'Mesenchymal stem cells'),
    (7, 'Hematopoietic stem cells'),
    (8, 'Pluripotent stem cells'),
    (9, 'Multipotent stem cells'),
    (10, 'Unipotent stem cells')
]

marrowdonor_insert_query = "INSERT INTO marrowdonor (DonorID, CellularComposition) VALUES (%s, %s)"
cursor.executemany(marrowdonor_insert_query, marrowdonor_data)


# Inserting data into heartdonor table
heartdonor_data = [
    (1, None, 'O+', 'AntibodyA', '2023-01-15 08:00:00'),
    (2, None, 'A-', 'AntibodyB', '2023-02-20 10:30:00'),
    (3, None, 'B+', 'AntibodyC', '2023-03-25 12:45:00'),
    (4, None, 'AB+', 'AntibodyD', '2023-04-30 15:15:00'),
    (5, None, 'A+', 'AntibodyE', '2023-05-10 18:20:00'),
    (6, None, 'O-', 'AntibodyF', '2023-06-05 20:00:00'),
    (7, None, 'B-', 'AntibodyG', '2023-07-12 22:10:00'),
    (8, None, 'AB-', 'AntibodyH', '2023-08-18 09:30:00'),
    (9, None, 'A-', 'AntibodyJ', '2023-09-24 11:45:00'),
    (10, None, 'O+', 'AntibodyI', '2023-10-30 14:20:00')
]

heartdonor_insert_query = "INSERT INTO heartdonor (DonorID, DonorName, BloodType, Antibodies, TimeOfDeath) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(heartdonor_insert_query, heartdonor_data)

# Inserting data into hospital table
hospital_data = [
    (1, 'City Hospital'),
    (2, 'Metro Hospital'),
    (3, 'Apex Hospital'),
    (4, 'Royal Hospital'),
    (5, 'Grand Hospital'),
    (6, 'Star Hospital'),
    (7, 'Sunrise Hospital'),
    (8, 'Golden Hospital'),
    (9, 'Healing Hospital'),
    (10, 'Sunset Hospital')
]

hospital_insert_query = "INSERT INTO hospital (FacilityID, Name) VALUES (%s, %s)"
cursor.executemany(hospital_insert_query, hospital_data)

# Inserting data into departments table
departments_data = [
    (1, 'Cardiology'),
    (2, 'Neurology'),
    (3, 'Orthopedics'),
    (4, 'Pediatrics'),
    (5, 'Oncology'),
    (6, 'Gynecology'),
    (7, 'Dermatology'),
    (8, 'ENT'),
    (9, 'Psychiatry'),
    (10, 'Urology')
]

departments_insert_query = "INSERT INTO departments (DepartmentID, DepartmentName) VALUES (%s, %s)"
cursor.executemany(departments_insert_query, departments_data)

# Inserting data into the staff table
staff_data = [
    (11, 'Doctor', '1970-05-15', 'Dr. Rajesh Kumar', '1234567890', 1),
    (12, 'Doctor', '1975-08-20', 'Dr. Nisha Patel', '9876543210', 2),
    (13, 'Doctor', '1980-10-25', 'Dr. Anil Verma', '7890123456', 3),
    (14, 'Nurse', '1985-03-10', 'Nurse Ritu Singh', '3456789012', 4),
    (15, 'Nurse', '1988-07-18', 'Nurse Priya Sharma', '5678901234', 5),
    (16, 'Nurse', '1990-12-22', 'Nurse Rohit Gupta', '8901234567', 6),
    (17, 'Admin', '1982-09-05', 'Mr. Amit Kumar', '2345678901', 7),
    (18, 'Admin', '1987-11-30', 'Ms. Anita Singh', '4567890123', 8),
    (19, 'Admin', '1992-02-14', 'Mr. Rajesh Sharma', '6789012345', 9),
    (20, 'Admin', '1995-04-27', 'Ms. Meena Gupta', '9012345678', 10),
    (21, 'Intern', '1998-01-05', 'Dr. Ananya Singh', '1234567890', 1),
    (22, 'Intern', '1997-06-15', 'Dr. Rohan Verma', '9876543210', 2),
    (23, 'Intern', '1996-09-20', 'Dr. Priya Gupta', '7890123456', 3),
    (24, 'ManagementStaff', '1980-02-28', 'Mr. Abhishek Sharma', '2345678901', 7),
    (25, 'ManagementStaff', '1985-05-15', 'Ms. Sneha Patel', '4567890123', 8),
    (26, 'ManagementStaff', '1990-07-10', 'Mr. Ankit Verma', '6789012345', 9),
    (27, 'ManagementStaff', '1994-10-22', 'Ms. Pooja Singh', '9012345678', 10)
]

staff_insert_query = "INSERT INTO staff (StaffID, StaffType, DOB, Name, PhoneNumber, DepartmentID) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(staff_insert_query, staff_data)


# Inserting data into managementstaff table
managementstaff_data = [
    (1, 'HR Manager', 17),
    (2, 'Finance Manager', 18),
    (3, 'Operations Manager', 19),
    (4, 'IT Manager', 20)
]

managementstaff_insert_query = "INSERT INTO managementstaff (ManagementStaffID, Title, StaffID) VALUES (%s, %s, %s)"
cursor.executemany(managementstaff_insert_query, managementstaff_data)


# Inserting data into intern table
intern_data = [
    (1, 11, 'Medical College A', 21),
    (2, 12, 'Medical College B', 22),
    (3, 13, 'Medical College C', 23)
]

intern_insert_query = "INSERT INTO intern (InternID, SupervisingDoctor, MedicalSchool, StaffID) VALUES (%s, %s, %s, %s)"
cursor.executemany(intern_insert_query, intern_data)

# Inserting data into nurse table
nurse_data = [
    (11, 'Cardiology', 'NLN001', 14),
    (12, 'Emergency', 'NLN002', 15),
    (13, 'Pediatrics', 'NLN003', 16),
    (14, 'Surgery', 'NLN004', 17)
]

nurse_insert_query = "INSERT INTO nurse (NurseID, Ward, NursingLicenseNumber, StaffID) VALUES (%s, %s, %s, %s)"
cursor.executemany(nurse_insert_query, nurse_data)

# Inserting data into medicalinsurance table
medicalinsurance_data = [
    (1, 'Policy A', 'MI001', 500000.00, 'Active'),
    (2, 'Policy B', 'MI002', 500000.00, 'Active'),
    (3, 'Policy C', 'MI003', 500000.00, 'Active'),
    (4, 'Policy D', 'MI004', 500000.00, 'Active')
]

medicalinsurance_insert_query = "INSERT INTO medicalinsurance (PolicyHolderID, PolicyName, PolicyNumber, CoverageAmount, Status) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(medicalinsurance_insert_query, medicalinsurance_data)



# Inserting data into malpracticeinsurance table
malpracticeinsurance_data = [
    ('MP001', 'Dr. Rajesh Kumar', 1000000.00),
    ('MP002', 'Dr. Nisha Patel', 1000000.00),
    ('MP003', 'Dr. Anil Verma', 1000000.00)
]

malpracticeinsurance_insert_query = "INSERT INTO malpracticeinsurance (PolicyNumber, HolderName, CoverageAmount) VALUES (%s, %s, %s)"
cursor.executemany(malpracticeinsurance_insert_query, malpracticeinsurance_data)



# Inserting data into doctor table
doctor_data = [
    (11, 'Cardiologist', 'MD', None, None, None, 11),
    (12, 'Neurologist', 'MD', None, None, None, 12),
    (13, 'Orthopedic Surgeon', 'MD', None, None, None, 13)
]

doctor_insert_query = "INSERT INTO doctor (DoctorID, Specialization, EDQualification, MalpracticeInsurancePolicyNumber, MalpracticeInsuranceHolderName, MalpracticeInsuranceCoverageAmount, StaffID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(doctor_insert_query, doctor_data)

# Inserting data into the patient table
patient_data = [
    (1, 'Rakesh Patel', '1234567890', 'Male', 52),
    (2, 'Suman Sharma', '9876543210', 'Female', 53),
    (3, 'Anil Verma', '7890123456', 'Male', 70),
    (4, 'Sarita Gupta', '3456789012', 'Female', 61),
    (5, 'Vivek Singh', '5678901234', 'Male', 58),
    (6, 'Neha Kapoor', '8901234567', 'Female', 67),
    (7, 'Amit Kumar', '2345678901', 'Male', 45),
    (8, 'Anita Singh', '4567890123', 'Female', 63),
    (9, 'Rajesh Sharma', '6789012345', 'Male', 42),
    (10, 'Meena Gupta', '9012345678', 'Female', 55)
]

patient_insert_query = "INSERT INTO patient (PatientID, Name, PhoneNumber, Gender, Age) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(patient_insert_query, patient_data)


# Inserting data into insuranceclaim table
insuranceclaim_data = [
    (15, 1, 'MI001', '2024-04-01', 25000.00, 'Approved', 'Processed successfully'),
    (16, 2, 'MI002', '2024-04-05', 30000.00, 'Pending', 'Under review'),
    (17, 3, 'MI003', '2024-04-10', 20000.00, 'Denied', 'Insufficient documentation'),
    (18, 1, 'MI001', '2024-04-15', 35000.00, 'Approved', 'Processed and approved'),
    (19, 2, 'MI002', '2024-04-20', 40000.00, 'Pending', 'Waiting for additional information'),
    (20, 3, 'MI003', '2024-04-25', 50000.00, 'Denied', 'Rejected due to policy terms'),
    (21, 4, 'MI004', '2024-04-30', 45000.00, 'Approved', 'Processed and approved')
]

insuranceclaim_insert_query = "INSERT INTO insuranceclaim (ClaimID, PatientID, PolicyNumber, DateOfClaim, AmountClaimed, Status, Remarks) VALUES (%s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(insuranceclaim_insert_query, insuranceclaim_data)


# Inserting data into vitals table
vitals_data = [
    (1, 1, 'O+', 'AntibodyA', 52, 1, 0, 125, 212, 0, 1, 168, 0, 1, 2, 2, 3),
    (2, 2, 'A-', 'AntibodyB', 53, 1, 0, 140, 203, 1, 0, 155, 1, 3.1, 0, 0, 3),
    (3, 3, 'B+', 'AntibodyC', 70, 1, 0, 145, 174, 0, 1, 125, 1, 2.6, 0, 0, 3),
    (4, 4, 'AB-', 'AntibodyD', 61, 1, 0, 148, 203, 0, 1, 161, 0, 0, 2, 1, 3),
    (5, 5, 'O-', 'AntibodyE', 58, 0, 0, 100, 248, 0, 0, 122, 0, 1, 1, 0, 2),
    (6, 6, 'A+', 'AntibodyF', 67, 0, 0, 106, 223, 0, 1, 142, 0, 0.3, 2, 2, 2),
    (7, 7, 'B-', 'AntibodyG', 45, 1, 0, 104, 208, 0, 0, 148, 1, 3, 1, 0, 2),
    (8, 8, 'AB+', 'AntibodyH', 63, 0, 2, 135, 252, 0, 0, 172, 0, 0, 2, 0, 2),
    (9, 9, 'O+', 'AntibodyI', 42, 0, 2, 120, 209, 0, 1, 173, 0, 0, 1, 0, 2),
    (10, 10, 'A-', 'AntibodyJ', 55, 1, 0, 130, 214, 0, 1, 159, 0, 0.8, 2, 0, 3)
]

vitals_insert_query = "INSERT INTO vitals (VitalsID, PatientID, BloodType, Antibodies, Age, Gender, CP, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(vitals_insert_query, vitals_data)

# Inserting data into cases table
cases_data = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10)
]

cases_insert_query = "INSERT INTO cases (CaseID, PatientID) VALUES (%s, %s)"
cursor.executemany(cases_insert_query, cases_data)


# Inserting data into files table
files_data = [
    (11, 1, 'MRI Scan', 'MRI scan report attached'),
    (12, 2, 'X-Ray', 'X-ray report attached'),
    (13, 3, 'Blood Test', 'Blood test results attached'),
    (14, 4, 'CT Scan', 'CT scan report attached'),
    (15, 5, 'Ultrasound', 'Ultrasound report attached'),
    (16, 6, 'ECG', 'ECG report attached'),
    (17, 7, 'Biopsy', 'Biopsy report attached'),
    (18, 8, 'Endoscopy', 'Endoscopy report attached'),
    (19, 9, 'Histopathology', 'Histopathology report attached'),
    (20, 10, 'Echocardiogram', 'Echocardiogram report attached')
]

files_insert_query = "INSERT INTO files (FileID, CaseID, FileType, Content) VALUES (%s, %s, %s, %s)"
cursor.executemany(files_insert_query, files_data)

# Inserting data into branch table
branch_data = [
    (1, 1, 'New Delhi'),
    (2, 2, 'Mumbai'),
    (3, 3, 'Bangalore'),
    (4, 4, 'Kolkata'),
    (5, 5, 'Chennai'),
    (6, 6, 'Hyderabad'),
    (7, 7, 'Pune'),
    (8, 8, 'Ahmedabad'),
    (9, 9, 'Jaipur'),
    (10, 10, 'Lucknow')
]

branch_insert_query = "INSERT INTO branch (BranchID, HospitalFacilityID, Location) VALUES (%s, %s, %s)"
cursor.executemany(branch_insert_query, branch_data)





# Inserting data into holds table
holds_data = [
    (11, 'MP001'),
    (12, 'MP002'),
    (13, 'MP003')
]

holds_insert_query = "INSERT INTO holds (DoctorID, PolicyNumber) VALUES (%s, %s)"
cursor.executemany(holds_insert_query, holds_data)
# Inserting data into donation table
donation_data = [
    (1, 1, 50000.00, 'Rajesh Sharma'),
    (2, 2, 70000.00, 'Priya Patel'),
    (3, 3, 45000.00, 'Amit Singh'),
    (4, 4, 60000.00, 'Reena Gupta'),
    (5, 5, 80000.00, 'Rahul Kumar'),
    (6, 6, 55000.00, 'Neha Sharma'),
    (7, 7, 75000.00, 'Ankit Verma'),
    (8, 8, 40000.00, 'Sonia Jain'),
    (9, 9, 65000.00, 'Vivek Gupta'),
    (10, 10, 85000.00, 'Meera Singh')
]

donation_insert_query = "INSERT INTO donation (DonationID, HospitalFacilityID, Amount, DonorName) VALUES (%s, %s, %s, %s)"
cursor.executemany(donation_insert_query, donation_data)



db_connection.commit()

# Closing cursor and database connection
cursor.close()
db_connection.close()