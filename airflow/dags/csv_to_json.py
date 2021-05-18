
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from random import randint
from datetime import datetime
import subprocess
import datetime as dt

from sqlalchemy import create_engine
import psycopg2
import pandas as pd


import csv
import pandas as pd 


host="172.26.0.2" # use, 172.26.0.2, "localhost" if you access from outside the localnet decompose env 
database="testDB"
user="me"
password="1234"
port='5432'
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
def _check_db_tables():
    print(engine.table_names())
   
def create_fake_data():
    #output=open('data1.csv','w')
    #fake=Faker()
    #header=['name','age','street','city','state','zip','lng','lat']
    #mywriter=csv.writer(output)
    #mywriter.writerow(header)
    #for r in range(200):
     #   row =[fake.name(),fake.random_int(min=18,max=80, step=1), 
      #                 fake.street_address(), fake.city(),fake.state(),
       #                fake.zipcode(),fake.longitude(),fake.latitude()]
        #mywriter.writerow(row)
    #output.close()
    DF=pd.read_csv('data.csv')

def data_to_postgres():
    DF.to_sql('users2021', engine, if_exists='replace',index=False)

def csv_to_json():
    for i,j in DF2.iterrows():
        print(j['name'])
    DF2.to_json('/opt/airflow/dags/fake.json',orient='records')



with DAG('csv_to_json',start_date=datetime(2021, 1, 1),
    schedule_interval="@daily",  
        catchup=False  
         ) as dag:
 
    create_fake_data = PythonOperator(task_id='creating',
                             python_callable=create_fake_data)
    
    data_to_postgres = PythonOperator(task_id='data_to_postgres',
                             python_callable=data_to_postgres)
    
    csv_to_json = PythonOperator(task_id='csv_to_json',
                             python_callable=csv_to_json)
    

 
 

create_fake_data >> data_to_postgres >> csv_to_json 

