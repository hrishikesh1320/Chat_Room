import threading  
import socket  

alies = input("Enter your nickname: ")  
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket object for client-side communication
client.connect(('localhost', 2013))  # Connecting to the server on localhost at port 2013

# Function to receive messages from the server
def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')  # Receiving messages from the server

            if message == "nickname":
                client.send(alies.encode('utf-8'))  # Sending the user's nickname to the server
            else:
                print(message)  # Printing received messages from other clients
        except Exception as e:
            print(f'Error: {e}')  # Handling and printing any exceptions
            client.close()  
            break

# Function to send messages to the server
def client_send():
    while True:
        message = f'{alies}: {input("")}'  # Allowing the user to input messages
        client.send(message.encode('utf-8'))  # Sending the user's message to the server

receive_thread = threading.Thread(target=client_receive)  # Creating a thread for receiving messages
receive_thread.start()  

send_thread = threading.Thread(target=client_send)  # Creating a thread for sending messages
send_thread.start() 
