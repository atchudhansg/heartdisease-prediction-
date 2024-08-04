
import mysql.connector

# Function to establish connection to MySQL database
def connect_to_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="hari",
            password="hari4114",
            database="HospitalManagementSystem"
        )
        print("Connected to MySQL server")
        return conn
    except mysql.connector.Error as err:
        print("Error:", err)
        return None

# Function to create database
def create_database(conn, database_name):
    try:
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        database_exists = False
        for db in databases:
            if db[0] == database_name:
                database_exists = True
                break

        # Create the database if it doesn't exist
        if not database_exists:
            cursor.execute("CREATE DATABASE " + database_name)
            print("Database '{}' created successfully".format(database_name))
        else:
            print("Database '{}' already exists".format(database_name))

        cursor.close()
    except mysql.connector.Error as err:
        print("Error:", err)

# Function to create tables for all entities
def create_tables(conn):
    if conn is None:
        print("Failed to connect to database")
        return

    try:
        cursor = conn.cursor()

        # Create Patient table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patient (
                PatientID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255) NOT NULL,
                PhoneNumber VARCHAR(20),
                Gender VARCHAR(10),
                Age INT
            )
        """)

        # Create Vitals table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Vitals (
                VitalsID INT AUTO_INCREMENT PRIMARY KEY,
                PatientID INT,
                BloodType VARCHAR(10),
                Antibodies VARCHAR(50),
                Age INT,
                Gender VARCHAR(10),
                CP INT,
                Trestbps INT,
                Chol INT,
                Fbs INT,
                Restecg INT,
                Thalach INT,
                Exang INT,
                Oldpeak FLOAT,
                Slope INT,
                Ca INT,
                Thal INT,
                Target INT,
                FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
            )
        """)

        # Create Departments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Departments (
                DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
                DepartmentName VARCHAR(255)
            )
        """)

        # Create Staff table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Staff (
                StaffID INT AUTO_INCREMENT PRIMARY KEY,
                StaffType VARCHAR(50),
                DOB DATE,
                Name VARCHAR(255),
                PhoneNumber VARCHAR(20),
                DepartmentID INT,
                FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
            )
        """)

        # Create Cases table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cases (
                CaseID INT AUTO_INCREMENT PRIMARY KEY,
                PatientID INT,
                FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
            )
        """)

        # Create Doctor table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctor (
                DoctorID INT AUTO_INCREMENT PRIMARY KEY,
                Specialization VARCHAR(255),
                EDQualification VARCHAR(255),
                MalpracticeInsurancePolicyNumber VARCHAR(50),
                MalpracticeInsuranceHolderName VARCHAR(255),
                MalpracticeInsuranceCoverageAmount DECIMAL(10, 2),
                StaffID INT,
                FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
            )
        """)

        # Create Nurse table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Nurse (
                NurseID INT AUTO_INCREMENT PRIMARY KEY,
                Ward VARCHAR(100),
                NursingLicenseNumber VARCHAR(50),
                StaffID INT,
                FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
            )
        """)

        # Create Intern table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Intern (
                InternID INT AUTO_INCREMENT PRIMARY KEY,
                SupervisingDoctor INT,
                MedicalSchool VARCHAR(255),
                StaffID INT,
                FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
            )
        """)

        # Create ManagementStaff table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ManagementStaff (
                ManagementStaffID INT AUTO_INCREMENT PRIMARY KEY,
                Title VARCHAR(100),
                StaffID INT,
                FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
            )
        """)

        # Create Files table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Files (
                FileID INT AUTO_INCREMENT PRIMARY KEY,
                CaseID INT,
                FileType VARCHAR(100),
                Content TEXT,
                FOREIGN KEY (CaseID) REFERENCES Cases(CaseID)
            )
        """)

        # Create MalpracticeInsurance table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MalpracticeInsurance (
                PolicyNumber VARCHAR(50) PRIMARY KEY,
                HolderName VARCHAR(255),
                CoverageAmount DECIMAL(10, 2)
            )
        """)

        # Create Holds table (Many-to-Many relationship between Doctor and MalpracticeInsurance)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Holds (
                DoctorID INT,
                PolicyNumber VARCHAR(50),
                FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
                FOREIGN KEY (PolicyNumber) REFERENCES MalpracticeInsurance(PolicyNumber)
            )
        """)

        # Create Hospital table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Hospital (
                FacilityID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255)
            )
        """)

        # Create Branch table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Branch (
                BranchID INT AUTO_INCREMENT PRIMARY KEY,
                HospitalFacilityID INT,
                Location VARCHAR(255),
                FOREIGN KEY (HospitalFacilityID) REFERENCES Hospital(FacilityID)
            )
        """)

        # Create Donation table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Donation (
                DonationID INT AUTO_INCREMENT PRIMARY KEY,
                HospitalFacilityID INT,
                Amount DECIMAL(10, 2),
                DonorName VARCHAR(255),
                FOREIGN KEY (HospitalFacilityID) REFERENCES Hospital(FacilityID)
            )
        """)

        # Create MedicalInsurance table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MedicalInsurance (
                PolicyHolderID INT AUTO_INCREMENT PRIMARY KEY,
                PolicyName VARCHAR(255),
                PolicyNumber VARCHAR(50),
                CoverageAmount DECIMAL(10, 2),
                Status VARCHAR(50),
                INDEX (PolicyNumber)  -- Add index on PolicyNumber column
            )
        """)

        # Create InsuranceClaim table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS InsuranceClaim (
                ClaimID INT AUTO_INCREMENT PRIMARY KEY,
                PatientID INT,
                PolicyNumber VARCHAR(50),
                DateOfClaim DATE,
                AmountClaimed DECIMAL(10, 2),
                Status VARCHAR(50),
                Remarks TEXT,
                FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
                FOREIGN KEY (PolicyNumber) REFERENCES MedicalInsurance(PolicyNumber)
            )
        """)

        # Create DonorBank table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS DonorBank (
                DonorBankID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255)
            )
        """)

        # Create Donor table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Donor (
                DonorID INT AUTO_INCREMENT PRIMARY KEY,
                DonorName VARCHAR(255),
                DonorBankID INT,
                FOREIGN KEY (DonorBankID) REFERENCES DonorBank(DonorBankID)
            )
        """)

        # Create BloodDonor table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BloodDonor (
                DonorID INT PRIMARY KEY,
                BloodType VARCHAR(10),
                FOREIGN KEY (DonorID) REFERENCES Donor(DonorID)
            )
        """)

        # Create HeartDonor table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS HeartDonor (
                DonorID INT PRIMARY KEY,
                DonorName VARCHAR(255),
                BloodType VARCHAR(10),
                Antibodies VARCHAR(50),
                TimeOfDeath DATETIME,
                FOREIGN KEY (DonorID) REFERENCES Donor(DonorID)
            )
        """)


        # Create MarrowDonor table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MarrowDonor (
                DonorID INT PRIMARY KEY,
                CellularComposition VARCHAR(255),
                FOREIGN KEY (DonorID) REFERENCES Donor(DonorID)
            )
        """)

        print("Tables created successfully")

        conn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print("Error:", err)

# Main function
    # Connect to MySQL server
conn = connect_to_database()
if conn is None:
    print("failed")




    # Create database tables
create_tables(conn)

    # Close connection
conn.close()
print("Connection to MySQL server closed")




