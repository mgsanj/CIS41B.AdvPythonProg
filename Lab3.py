import socket  # Import socket module
from tkinter import *
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import sqlite3
import json
import os

sqliteConnection = None

        
class backendService:
    def __init__(self, country):
        self.country = country
        self.tableN = "UNData"
        self.data = self.build_query_forACountry()
        
    def build_query_forACountry(self):
        query = "SELECT * FROM {} where Country = '{}'".format(self.tableN, self.country)
        data = databaseService().search(query)
        return data
        
    
class databaseService:
    def __init__(self):
        self.dbName = "Lab3.db" #make into paramters
        self.tableN = "UNData" #make into paramters
        
    def construct(self):
        self.connect()                                  #connect database
        
        #parse data
        file = open("/Users/SanjanaGadaginmath/Downloads/UNData (1).xml", "r")
        contents = file.read()
        soup = BeautifulSoup(contents, 'xml')
        records = soup.find_all("record")
        countries = []
        years = []
        values = []
        num = 0
        for record in records:
            values.append(record.find("Value").text)
            country = record.find("Country").text
            year = record.find("Year").text
            for i in countries:
                if i == country:
                    country = None
            for j in years:
                if j == year:
                    year = None
            if country != None:
                countries.append(country)
            if year != None:
                years.append(year)
        
        #create SQL queries and insert data
        string = ""
        for i in years:
            if i == years[-1]:
                string += "'{}' INT".format(i)
            else:
                string += "'{}' INT, ".format(i)
        query = "CREATE TABLE {} ('Country' STRING, {})".format(self.tableN, string)
        self.table(query)                        #create table
        query = "INSERT INTO {} ('Country',".format(self.tableN)
        for year in years:
            if year == years[-1]:
                query += f" '{year}') VALUES ("
            else:
                query += f" '{year}',"
        
        for country in countries:
            insert_query = query
            data = []
            for i in range(28):
                data.append(values[0])
                values.pop(0)
            insert_query += f"'{country}', "
            for i in data:
                if i == data[-1]:
                    insert_query += f" {i})"
                else:
                    insert_query += f" {i}," 
            self.insert(insert_query)            #insert data
        return countries, years
        
        
    def connect(self):
        global sqliteConnection
        try:
            sqliteConnection = sqlite3.connect(self.dbName)
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            select_Query = "select sqlite_version();"
            cursor.execute(select_Query)
            record = cursor.fetchall()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)         
        
    def table(self, query):
        global sqliteConnection
        try:
            cursor = sqliteConnection.cursor()
            cursor.execute(query)
            sqliteConnection.commit()
            print("SQLite table created")    
        except sqlite3.Error as error:
            print("Table exists: ", error)
        
        
    def insert(self, query):
        global sqliteConnection
        try:
            cursor = sqliteConnection.cursor()
            cursor.execute(query)
            sqliteConnection.commit()
            print("Inserted successfully into table")
        except sqlite3.Error as error:
            print("Failed to insert: ", error)  
            
    def search(self, query):
        global sqliteConnection
        try:
            cursor = sqliteConnection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result        
        except sqlite3.Error as error:
            print("Country not found: ", error)
        

class server():
    def __init__(self, portnumber):
        self.port = portnumber                    # Reserve a port for your service every new transfer wants a new port or you must wait.
        self.sktServer = socket.socket()             # Create a socket object
        self.host = socket.gethostname()   # Get local machine name
        self.sktServer.bind((self.host, self.port))            # Bind to the port
        self.sktServer.listen(1)    
        self.connect()                  # Now wait for client connection.
        
    def connect(self):
        print('Server listening....')
        global conn, addr 
        conn, addr = self.sktServer.accept() 
        print(addr)       
    
    def SendData(self, json):
        
        while True:     # Establish connection with client.
            print('Connected to', addr)
            
            message = json.encode('UTF-8')  #send data
            print('sending {!r}'.format(message))
            
            conn.sendall(message)
            print('Done sending')
            break
            
    def GetData(self):
        JSONstring = ""
        
        while True:
            global conn
            data = conn.recv(1024)
            print('Server received', repr(data))
            if not data:
                break            
            JSONstring += data.decode("utf-8")
            break
            
        string = json.loads(JSONstring)
        return string
          
if __name__ == "__main__":
    countries, years = databaseService().construct() #send countries to client
    
    ser = server(3262)
    ser.SendData(json.dumps(countries))
    country = ser.GetData()
    data = list(backendService(country).data[0])
    ser.SendData(json.dumps(data))
    ser.SendData(json.dumps(years))
    
    
    #ser.SendData()


