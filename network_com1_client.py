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
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define a message to send
message = "Hello, UDP server, hello!"

# Send the message to the server
client_socket.sendto(message.encode(), (server_ip, server_port))

# Receive a response from the server
response, server_address = client_socket.recvfrom(1024)
print(f"Received from server: {response.decode()}")

# Close the socket
end_message = "close socket"
client_socket.sendto((end_message.lower()).encode(), (server_ip, server_port))

close_response, server_address = client_socket.recvfrom(1024)
if (close_response.decode() == "Closing..."):
    client_socket.close()
 