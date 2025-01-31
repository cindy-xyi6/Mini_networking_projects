import socket
import Encrypt_Decrypt_Class as Encrypt_message
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

encrypt_increment = 6
message = Encrypt_message.Encrypt_Decrypt(encrypt_increment)

# Create a UDP socket
friend1_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# self.encypt_increment: generates a random value to increment the ascii char value by.
conversation_socket = "open"

while (conversation_socket == "open"):
    # Define a message to send
    friend1_message = input("What message do you want to send to friend2?('bye' to close socket.) ")

    if (friend1_message == "bye"):
        conversation_socket = "close"
        end_message = "end"
        Encrypted_message = message.Encrypt(end_message)
        friend1_socket.sendto(Encrypted_message.encode(), (server_ip, server_port))
        friend1_socket.close()
        print("Conversation ended!")
        
    else:
        Encrypted_message = message.Encrypt(friend1_message)
        # Send the message to the server
        friend1_socket.sendto(Encrypted_message.encode(), (server_ip, server_port))

        # Receive a response from the server
        response, server_address = friend1_socket.recvfrom(1024)
        print(f"Received from friend2: {response.decode()}")

file.close()

# Create 3rd agent that receives encrypted message, prints it. 
# Then sends it to server and server decrypts it and prints to show full process.
# Extra : Connect ip address and any relevent info to either start or end of message, in which
#       3rd agent reads to know where to send the message to.
