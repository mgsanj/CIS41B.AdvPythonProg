from urllib.request import urlopen
import re
import pandas as pd
import json
import socket

# --------- question 1 ------------
class Parser():

    def __init__(self, site):
        opened = urlopen(site)
        self.data = opened.read().decode('utf-8')
        
    def findData(self):
        #getting data
        itera = 0
        data = []
        for line in self.data.split("\n"):
            if len(line) >= 1:
                if line[0] == ' ':
                    data.append(line.split())
                if line[0] == '#':
                    itera += 1
        self.data = self.data.split("\n")
        
        #getting column names
        cols = [re.split('\s{2,}', self.data[itera-2])[1:], re.split('\s{2,}', self.data[itera-1])[1:]]
        cols[1].insert(3, " ")
        col = []
        for i in range(len(cols[0])):
            col.append(cols[0][i] + " " + cols[1][i])
        col.insert(0, "year")
        col.insert(1, "month")
        
        #creating dataframe and then converting to JSON string
        df = pd.DataFrame(data, columns = col)
        json = df.to_json()
        
        return json
#----------- question 2 ----------------
class Server:
    def __init__(self,port):
        self.host = socket.gethostname()
        self.port = port  # initiate port no above 1024
        self.server_socket = socket.socket()  # get instance
        self.server_socket.bind((self.host, self.port))  # bind host address and port together
    def Connect(self,nports,json):
        # configure how many client the server can listen simultaneously
        self.server_socket.listen(nports)
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            print('Server received', repr(data))
        
            message = json.encode('UTF-8')
            print('sending {!r}'.format(message))
            sock.sendall(message)
           
            print("from connected user: " + str(data))
            conn.send(data.encode())  # send data to the client
        conn.close()  # close the connection
# ------------- question 3 ------------------    
class Client:
    def __init__(self,nport):
        self.host = socket.gethostname()  # as both code is running on same pc
        self.port = nport  # socket server port number
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((self.host, self.port))  # connect to the server
    def Connect(self):
        message = input(" -> ")  # take input
        while message.lower().strip() != 'bye':
            data = self.client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
            message = input(" -> ")  # again take input
        self.client_socket.close()  # close the connection

# ------------ question 5 ----------------------       
'''
cookiejar = queue.Queue()
condition = threading.Condition()

clientList = []
serverList = []

class ConsumerThread(threading.Thread):
    def run(self):
        global cookiejar
        condition.acquire()
        print("<<client lock acquired>>")
        if not cookiejar.empty():
            chip = cookiejar.get()
            print("client consumed", chip)
        else:
            condition.wait()
        condition.release()
        print(">>client released<<")
        time.sleep(0.1)
            
class ProducerThread(threading.Thread):
    def run(self):
        global data
        global cookiejar
        condition.acquire()
        print("<<server lock acquired>>")
        if cookiejar.empty():
            cookiejar.put(data)
            print("server", data)
            print(">>server lock released<<")
            time.sleep(0.1)
        condition.notify()
        condition.release()        


nruns = (len(json.encode('UTF-8')) // 1024) + 1
for pc in range(nruns):            
    clientList.append(ProducerThread())
    serverList.append(ConsumerThread())
    
for pc in range(nruns):            
    clientList[pc].start()
    serverList[pc].start()
    
for pc in range(nruns):            
    clientList[pc].join()
    serverList[pc].join() 

 '''

            
    
        
if __name__  == "__main__":
    url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"
    json = Parser(url).findData()
    server = Server(2785)
    server.Connect(1, json) 
    client = Client(2785)
    client.Connect()    
        
