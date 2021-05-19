import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# host = localhost
host = input("Please enter the IP address of server: ")

s.connect((host, 5000)) # connect to the specified port (should be the port of the server)
print(s.recv(1024).decode()) # receive the acknowledgement from the server

while True: 
    print(s.recv(1024).decode(), end="") # server prompts for input
    input_text = input()
    s.send(input_text.encode()) # send input to server
    print(input_text, " in Pig Latin is: ", s.recv(1024).decode()) # receive translated word/s
    print(s.recv(1024).decode(), end="") # server asks to continue? prompt
    proceed = input() # answer to continue? prompt
    s.send(proceed.encode()) # send response to server

    if proceed == "n":
        s.close() # if response is n, we terminate the connection to the server
        break # end the loop too