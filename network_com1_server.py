import socket
import os
curr_dir = os.getcwd()
target_dir = "C:/Users/cindy/Documents/Python/Mini_networking_projects"
os.chdir(target_dir)

# Define the server IP and port (Reading from a text file.)
file = open("Ip_and_port.txt", "r")
Ip_and_Port = file.readlines()
server_ip = Ip_and_Port[0].removeprefix("Server_Ip: ")
server_ip = server_ip.removesuffix("\n")
server_port = int(Ip_and_Port[1].removeprefix("Server_Port: "))

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))
socket_status = "opened"

print(f"UDP server up and listening on {server_ip}:{server_port}")

# Loop to listen for incoming datagrams
while (socket_status == "opened"):
    # Receive message from client
    message, client_address = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
    print(f"Received message from {client_address}: {message.decode()}")
    
    # Send a response back to the client
    response_message = "Message received, hello!"
    server = server_socket.sendto(response_message.encode(), client_address)

    end_message, client_address = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
    # When receives "close socket" from client the server_socket will close.
    if (end_message.decode() == "close socket"):
        close_response = "Closing..."
        print(close_response)
        server_socket.sendto(close_response.encode(), client_address)
        server_socket.close()
        socket_status = "closed"


