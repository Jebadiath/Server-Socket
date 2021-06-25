#!/usr/bin/python3

import socket #Running on computer, bound to specific port - Server listens to this waiting for a client to make a connection.

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Imported socket module, created socket function, specified socket type

host = socket.gethostname() #Automated function to get IP
port = 444

serversocket.bind((host, port)) #Host will be replaced/substituted with IP, if changed and not running on host

serversocket.listen(2) #TCP Listener (up to a max of 2 connections)

while True: #While this is true
    clientsocket, address = serversocket.accept() #Starting Connection

    print("received connection from " % str(address)) 
    
    message = 'Hello! Thank you for visiting my first Python project!' + "\r\n" #Message sent to client
    clientsocket.send(message.encode('ascii')) #Actioned to send data

    clientsocket.close()
