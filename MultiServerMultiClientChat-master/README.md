# MultiServerMultiClientChat
Multi Client Multi Server Chat Application in Python with Load Balancing and Reliability

The objective of this application is to develop a multi-server chat i.e. multiple co-operating servers with location transparency. The application consists of multiple clients who can join to a front-end server using its IP address. Front-end sever manages multiple backend servers for reliability and Load Balancing. There are two or more backend servers which handle client requests and respond to all active clients. I have also encrypted and decrypted the chat for security.

For this application, I have implemented multi-server chat with reliability and Load Balancing. For reliability, if one of the backend servers is crashed or terminated, the other server handles the request from clients. For Load Balancing, the requests from clients are balanced to the backend server by the front end server based on a number of clients and size of the message as the critical factors. If the message length is greater than 7 then by default the messages are sent to Primary Server 1. If the primary server is not running, then the request is sent to Primary Server 2.

Design Approach and Justification: 
I developed this application in python. I have three applications for 

•	Client 
•	Front-end server 
•	Back-end server (1-4)

Client:
Client will be prompted to enter the IP address of the front-end server to connect to the chat application. Once correct IP address is entered, front-end server adds the client address to a list and it creates a connection with the client. Multiple clients can send request to frontend server. Client application runs two threads- one for sending messages and other for receiving message from different clients. 

Front-end server:
There is one front-end server running in our application. It receives the entire request from clients and forwards it to multiple backend servers. It keeps track of connected backend servers in a list and a flag to check the connection status of the backend server. It has three threads running in parallel. First thread is to monitor backend server. Second thread is to receive messages from clients. Third is to update the client list to active backend servers. 

Backend server:
There are four replicated backend servers running in different machines to handle reliability and load balancing. These backend servers receives request from frontend server and sends only to connected clients. 

Config file:
The config file has the list of primary and secondary server with its corresponding IP address. The data is given to frontend server.

