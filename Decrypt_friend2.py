import socket
import Encrypt_Decrypt_Class as Decrypt_message
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

decrypt_increment = 6
message = Decrypt_message.Encrypt_Decrypt(decrypt_increment)

# Create a UDP socket (friend2 = server)
friend2_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
friend2_socket.bind((server_ip, server_port))
socket_status = "opened"

print(f"UDP server up and listening on {server_ip}:{server_port}")
  
# Loop to listen for incoming datagrams
while (socket_status == "opened"):
    # Receive message from client
    received_message, client_address = friend2_socket.recvfrom(1024)  # Buffer size of 1024 bytes
    print(received_message.decode())
    Original_message = message.Decrypt(received_message.decode())

    if (Original_message == "end"):
        socket_status = "closed"
    else:
        print(f"Received message from 'Friend1'{client_address}: {Original_message}")
        # Send a response back to the client
        response_message = "Message received, hello!"
        friend2_socket.sendto(response_message.encode(), client_address)
        # When receives "close socket" from client the server_socket will close.

friend2_socket.close()
print("Bye...")  

file.close()