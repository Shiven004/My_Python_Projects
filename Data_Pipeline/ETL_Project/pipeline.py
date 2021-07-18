#!/usr/bin/python3
"""This data pipeline uses movie lens database. Takes MySQL data and puts it into mongoDB"""

# Author : Shivender 17/07/2021

# System libs
import copy

# External Libs
import psycopg2
from pymongo import MongoClient
import pymysql

# Internal libs
import config


# Pipeline constants
RESET_MONGO_COLLECTIONS_ON_UPDATE = True # Resets the collections if a collection already exists, if false, the data is appeneded to the collection
PRINT_INFO = True # Print options for debugging purposes
PRINT_RESULTS = True # Print option for debugging purposes

def initalise_mysql():
    """Initalises and returns a MySQL database based on config"""
    return pymysql.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USERNAME,
        password=config.MYSQL_PASSWORD,
        db=config.MYSQL_DB)

def initalise_mongo():
    """Initializes and returns mongoDB database based on config"""
    return MongoClient(config.MONGO_HOST, config.MONGO_PORT)[config.MONGO_DB]    

def extract_data(mysql_cursor):
    """Given a cursor, Extracts data from MySQL movielens dataset
    and returns all the tables with their data"""    
    movies = execute_mysql_query('select * from movies', mysql_cursor, 'fetchall')
    ratings = execute_mysql_query('select * from ratings', mysql_cursor, 'fetchall')    
    tables = (movies, ratings)
    return tables

def execute_mysql_query(sql, cursor, query_type):
    """exectues a given sql, pymysql cursor and type"""
    if query_type == "fetchall":
        cursor.execute(sql)
        return cursor.fetchall()
    elif query_type == "fetchone":
        cursor.execute(sql)
        return cursor.fetchall()
    else:
        pass

def transform_data(dataset, table):
    """Transforms the data to load it into mongoDB, returns a JSON object"""
    dataset_collection = []
    tmp_collection = {}    
    if table == "movies":
        for item in dataset[0]:
            tmp_collection['movieId'] = item[0]
            tmp_collection['title'] = item[1]
            tmp_collection['genres'] = item[2]            
            dataset_collection.append(copy.copy(tmp_collection))
        #return dataset_collection    
    if table == "ratings":
        for item in dataset[1]:
            tmp_collection['userId'] = item[0]
            tmp_collection['movieId'] = item[1]
            tmp_collection['rating'] = item[2]
            tmp_collection['timestamp'] = item[3]            
            dataset_collection.append(copy.copy(tmp_collection))             
    return dataset_collection
         

def load_data(mongo_collection, dataset_collection):
    """Loads the data into mongoDB and returns the results"""
    if RESET_MONGO_COLLECTIONS_ON_UPDATE:
        mongo_collection.delete_many({})
    return mongo_collection.insert_many(dataset_collection)

def main():
    """main method starts a pipeline, extracts data,
    transforms it and loads it into a mongo client"""
    if PRINT_INFO:
        print('Starting data pipeline')
        print('Initialising MySQL connection')
    mysql = initalise_mysql()
    
    if PRINT_INFO:
        print('MySQL connection Completed')
        print('Starting data pipeline stage 1 : Extracting data from MySQL')
    mysql_cursor = mysql.cursor()
    mysql_data = extract_data(mysql_cursor)
    
    if PRINT_INFO:
        print('Stage 1 completed! Data successfully extracted from MySQL')
        print('Starting data pipeline stage 2: Transforming data from MySQL for mongoDB')
        print('Transforming genres dataset')
    movies_collection = transform_data(mysql_data, "movies")
    
    if PRINT_INFO:
        print('Successfully transformed genres dataset')
        print('Transforming users dataset')
    ratings_collection = transform_data(mysql_data, "ratings")    
    
    if PRINT_INFO:
        print('Successfully transformed users dataset')
        print('Stage 2 completed! Data successfully transformed')
        print('Intialising mongoDB connection')
    mongo = initalise_mongo()
    print("-----Debugging------")
    print('mongo is :: ',mongo)
    print('type of mongo is :: ',type(mongo))    
    if PRINT_RESULTS:
        print('Successfully loaded users')        
    result = load_data(mongo['movies'], movies_collection)
    print(result)
    
    if PRINT_RESULTS:
        print('Successfully loaded users')        
    result = load_data(mongo['ratings'], ratings_collection)
    print(result)
    
    if PRINT_RESULTS:
        print('Successfully loaded users')
        print(result)
    
    if PRINT_INFO:
        print('Stage 3 completed! Data successfully loaded')
        print('Closing MySQL connection')
    mysql.close()
    if PRINT_INFO:
        print('MySQL connection closed successfully')
        print('Ending data pipeline')
    
if __name__ == "__main__":
    main()
