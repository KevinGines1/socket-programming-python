import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# host = localhost
host = input("Please enter the IP address of server: ")

s.connect((host, 5000)) # connect to the specified port (should be the port of the server)
print(s.recv(1024).decode())

while True: 
    print(s.recv(1024).decode(), end="") # prompt for input
    input_text = input()
    s.send(input_text.encode()) # send input to server
    print(input_text, " in Pig Latin is: ", s.recv(1024).decode()) # translated 
    print(s.recv(1024).decode(), end="") # continue? prompt
    proceed = input() # answer to continue? prompt
    s.send(proceed.encode()) # send response to server

    if proceed == "n":
        s.close() # if response is n, we terminate the connection
        break # end the loop too