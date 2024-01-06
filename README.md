**Chat Room using Socket Programming**

This repository contains a simple chat room application implemented in Python using socket programming. It allows multiple clients to connect to a server and exchange messages in real-time.

**Features**

Server-Client Model: Utilizes a server-client architecture for handling communication.
Multiple Connections: Allows multiple clients to connect to the server concurrently.
Nickname Management: Assigns nicknames to clients for identification within the chat room.

**Requirements**

Python 3.x
Libraries: socket, threading

****How to Use****
****Server****
Run the server script admin_server.py.
The server listens on a specified port for incoming client connections.

****Client****
Run the client script client.py.
Enter a nickname when prompted.
Start exchanging messages in the chat room.

****Implementation Details****
Server Side:
server.py: Sets up a server socket, manages client connections, and handles message broadcasting.
Client Side:
client.py: Connects to the server, sets a nickname, sends and receives messages.
