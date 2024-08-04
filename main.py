import ml_model
 
import mysql.connector

connection = mysql.connector.connect(
            host="localhost",
            user="hari",
            password="hari4114",
            database="HospitalManagementSystem"
)
cursor = connection.cursor()

print("Which Feature Do YOu Want to access?: ")
print("1) Heart Failure and Donor Matching")
print("2) Responsive Companion")
print("3) Enter zero to exit (0)")
choice=int(input("Enter the choice: "))
while(choice!=0):
    if(choice==1):
        n=int(input("Enter the Patient Id:"))
        sql_query = "SELECT * FROM vitals WHERE PatientID = %s;"
        cursor.execute(sql_query, (n,))
        row = cursor.fetchone()
        x_test=list(row[4:])
        target=x_test.pop()
        blood_type=row[2]
        antibody_type=row[3]
        flag=ml_model.run_model(x_test)
        if(flag==0):
            
            target=0
            sql_query = "UPDATE vitals SET Target = %s WHERE PatientID = %s;"
            cursor.execute(sql_query, (target,n))
            connection.commit()
        else:
            # Type O- type A,type A,B,AB,O
            # Type A- type A,type AB
            # Type B- type B,type AB 
            # Type AB-type AB
            query = "SELECT * FROM heartdonor WHERE BloodType = %s AND Antibodies = %s;"
            cursor.execute(query, (blood_type, antibody_type))
            results = cursor.fetchall()
            if(len(results)==0):
                print ("NO Matches Found")
            else:
                print(len(results)," Matches found")
                #fetch then anem of donor and bank info from respective tables
                for row in results:
                    print(row)    

       
           
        
    elif(choice==2):
        print()
    else:
        print("Incorrect Input")  

    choice=int(input("Enter the choice:"))      



print("Program Exited")


