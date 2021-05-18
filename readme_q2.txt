##1
#run the docker-compose file (for the pgadmin and the notebook)
docker-compose up

##2
#then go to the browser -->localhost:port
#open the pgadmin and the jupyter notebook 

##3
#in the jupyter notebook create fake date csv file
#read this data as a postgres table 
#back to the pgadmin page to see the table

##4
#covert the csv file to json file
#and after that push it to the mongo 

##5
put all the dependencies as a dag in the airflow

create_fake_data >> data_to_postgres >> csv_to_json >> json_to_mongo
