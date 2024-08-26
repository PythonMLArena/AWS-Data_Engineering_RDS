from dotenv import load_dotenv
import os
from rds_connection_raw import SimpleRDSDictConnector
load_dotenv()

DB_Username=os.getenv('rds_username')
DB_Password=os.getenv('rds_password')
DB_Endpoint=os.getenv("rds_endpoint")

connection=SimpleRDSDictConnector(user=DB_Username, password=DB_Password, host=DB_Endpoint)

output=connection.execute_query("CREATE DATABASE IF NOT EXISTS PRATHAMTEMP;")

print(output)

output=connection.execute_query("USE PRATHAMTEMP;")

print(output)

output=connection.execute_query("SHOW DATABASES;")

print(output)

output=connection.execute_query("SHOW TABLES;")

print(output)