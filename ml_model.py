import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def train_model():
    #read the csv
    df=pd.read_csv(r'C:\Users\harik\OneDrive\Desktop\dbms project\final_data.csv')
    #preparing the dependant and indepedant variable
    x=df.drop('target',axis=1)
    y=df['target']
    #train and test split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    # running the model
 
    model=GaussianNB()
    model.fit(x_train,y_train)
    
    return model

def run_model(x_test):
   #return the patient vitals
    columns = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 
    'fbs', 'restecg', 'thalach', 'exang', 
    'oldpeak', 'slope', 'ca', 'thal'
    ]
    data= pd.DataFrame(columns=columns)
    data.loc[len(data)] = x_test

    model=GaussianNB()
    model=train_model()
    y_predict=model.predict(data)
    
    if(y_predict[0]==1):
        print("Heart Failure")
        return 1
    else:
        print("Heart is fine")  
        return 0 



