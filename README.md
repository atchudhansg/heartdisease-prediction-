# Heart Disease Prediction - Database Management System Project

This repository focuses on designing and managing a **MySQL-based** database for heart disease prediction. The project includes scripts for setting up the database, inserting patient records, querying results, and integrating machine learning predictions into a structured database system.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Database Design](#database-design)
3. [Project Flow](#project-flow)
4. [File Descriptions](#file-descriptions)
   - [HeartFailure (1).ipynb](#heartfailure-1ipynb)
   - [dbms.py](#dbmspy)
   - [insertion.py](#insertionpy)
   - [main.py](#mainpy)
   - [ml_model.py](#ml_modelpy)
   - [tempCodeRunnerFile.py](#tempcoderunnerfilepy)
5. [Tech Stack](#tech-stack)
6. [Setup & Usage](#setup--usage)
7. [Contributors](#contributors)
8. [License](#license)

---

## Introduction

This project integrates a **MySQL Database Management System (DBMS)** to store, manage, and analyze heart disease patient records and predictions. The database acts as a **centralized structured storage**, ensuring **data consistency, integrity, and efficient retrieval**.

### Objectives:
- **Design a MySQL relational database** for heart disease records and predictions.
- **Create SQL-based operations** for inserting, retrieving, updating, and deleting records.
- **Use PyMySQL to interact with the database** in Python scripts.
- **Integrate the machine learning model** for predictive analysis and storage.
- **Ensure data integrity** using structured tables and constraints.

---

## Database Design

The project is structured using **MySQL** for efficient data storage and retrieval. Below is the database schema:

### Tables:

#### 1. `patients` (Stores basic patient details)
| Column Name    | Data Type  | Constraints        | Description |
|---------------|-----------|--------------------|-------------|
| patient_id    | INT       | PRIMARY KEY, AUTO_INCREMENT | Unique ID for each patient |
| name          | VARCHAR(100) | NOT NULL | Full name of the patient |
| age           | INT       | NOT NULL | Age of the patient |
| gender        | ENUM('Male', 'Female', 'Other') | NOT NULL | Gender of the patient |
| cholesterol   | FLOAT     | NOT NULL | Cholesterol level |
| blood_pressure| FLOAT     | NOT NULL | Blood pressure reading |
| diabetes      | BOOLEAN   | NOT NULL | Indicates if the patient has diabetes |
| created_at    | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |

#### 2. `predictions` (Stores model predictions)
| Column Name   | Data Type  | Constraints | Description |
|--------------|-----------|-------------|-------------|
| prediction_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique ID for each prediction |
| patient_id | INT | FOREIGN KEY REFERENCES patients(patient_id) ON DELETE CASCADE | Links prediction to a patient |
| risk_score | FLOAT | NOT NULL | Predicted probability of heart disease |
| predicted_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Time of prediction |

---

## Project Flow

1. **Database Setup & Configuration**  
   - Create and initialize the **patients** and **predictions** tables in MySQL.
   - Establish database connectivity using `dbms.py` via **PyMySQL**.
   - Ensure constraints and relationships are properly defined.

2. **Data Insertion & Management**  
   - Use `insertion.py` to add patient records into the database.
   - Maintain data integrity by handling constraints and avoiding duplicate entries.

3. **Querying & Analysis**  
   - Retrieve patient records for further analysis.
   - Fetch historical predictions and assess patient risk over time.

4. **Machine Learning Integration**  
   - Predict heart disease risk using `ml_model.py`.
   - Store predictions in the database for future reference.

5. **Application Execution**  
   - Use `main.py` to interact with both the database and the machine learning model.

---

## File Descriptions

### HeartFailure (1).ipynb
- Jupyter Notebook used for initial data analysis and testing different machine learning models.
- Includes feature engineering and visualization of patient data.

### dbms.py
- Handles all **MySQL database** operations using **PyMySQL**, including:
  - Connecting to the MySQL database.
  - Running SQL queries for data retrieval, insertion, and updates.
  - Ensuring proper error handling in database interactions.

### insertion.py
- Inserts patient records into the **MySQL database**.
- Ensures unique and valid patient information before storing data.

### main.py
- The central script that:
  - Retrieves patient records from **MySQL**.
  - Runs predictions using the trained ML model.
  - Stores the predicted risk scores back into the **MySQL database**.

### ml_model.py
- Contains the machine learning model for predicting heart disease risk.
- Loads patient data from **MySQL**, preprocesses it, and applies the trained model.
- Returns probability scores that indicate the likelihood of heart disease.

### tempCodeRunnerFile.py
- A temporary file auto-generated by the IDE.
- Can be ignored and removed.

---

## Tech Stack

- **Python (3.x)**
- **MySQL** (with PyMySQL for database interactions)
- **Pandas, NumPy** for data processing.
- **scikit-learn** for machine learning.
- **SQLAlchemy / PyMySQL** for database interactions.
- **Jupyter Notebook** for data analysis.

---

## Setup & Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/heart-disease-dbms.git
   cd heart-disease-dbms
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MySQL Database**:
   - Ensure MySQL is installed and running.
   - Create the database using:
     ```sql
     CREATE DATABASE heart_disease_db;
     ```
   - Update `dbms.py` with the database credentials.

4. **Run Database Initialization**:
   ```bash
   python dbms.py
   ```

5. **Insert Sample Data**:
   ```bash
   python insertion.py
   ```

6. **Run the Main Application**:
   ```bash
   python main.py
   ```

---

## Contributors

Contributors:

- **[Harii2K4](https://github.com/Harii2K4)**  
- **[KairavDeepeshwar](https://github.com/KairavDeepeshwar)**  

If you find this project useful or want to contribute, feel free to fork it or submit a pull request.

---

## License

Distributed under the [MIT License](LICENSE).
