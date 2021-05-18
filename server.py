import socket
#* ========================================= FUNCTIONS

# function that sets up the server
def setupServer():
    # create a socket object with TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        #use port 5000
        host = ''
        port = 5000
        s.bind((host, port)) # bind the port 5000 to the socket, host is blank so we can accept connection from other computer in the network
        print("Socket successfully created")
        print("Socket binded to ", port)
        s.listen()
        print("socket is listening")
        return s
    
    except socket.error as msg:
        print("Bind failed. Error Code: ", str(msg[0]), " Message: ", msg[1])

# function that converts a list of strings to pigLatin
def pigLatin(text):
    deconstruct = []
    translated = ""
    if " " in text: # if the input is a sentence
        deconstruct = text.split(" ")

        for word in deconstruct: # translate to piglatin every word
            translated = translated + pigLatinHelper(word)
            translated = translated + " "

    else: 
        translated = pigLatinHelper(text)

    return translated

# # function that returns true if all letters in a string is a constonant
def isAllConsonant(text):
    for letter in text:
        if letter in ["a", "e", "i", "o", "u"]:
            return False
    return True

# #function that converts input text to piglatin
def pigLatinHelper(text):

    normalized_text = text.lower()
    translation = normalized_text

    conso_clust = "" # consonant cluster

    # if first letter is a consonant
    if normalized_text[0] not in ["a", "e", "i", "o", "u"]:
        if isAllConsonant(normalized_text):
            translation = translation[len(translation)-1] + translation[0:len(translation)-1]
            translation = translation + "ay"
        else:
            for letter in normalized_text:
                if letter not in ["a", "e", "i", "o", "u"]:
                    conso_clust = conso_clust + letter
                    
                    translation = translation[1:len(translation)]
                else:
                    translation = translation + conso_clust
                    translation = translation + "ay"
                    break
        # translation = translation + conso_clust
        # translation = translation + "ay"
    else:
        translation = translation + "yay"
    

    return translation
#* ===================================================

s = setupServer()
message = "Successfully connected to the server"
prompt = "Please enter a word to translate to Pig Latin: "
cont = "Continue? (y/n): "
while True:
    
    c, addr = s.accept() # establish connection with client
    print("Got connection from ", addr)
    c.send(message.encode()) #acknowledge client of the connection

    proceed = "y"
    while proceed != "n":
        c.send(prompt.encode())
        input_text = c.recv(1024) # wait for an input
        input_text = input_text.decode()
        print("Input: ", input_text)

        trans_text = pigLatin(input_text)
        print("Output: ", trans_text)
        
        c.send(trans_text.encode()) # send translated word to client
        c.send(cont.encode()) # send continue? prompt
        proceed = c.recv(1024).decode()
    # c.close()



# while(connected):
#     # get input from client
#     text_input = input()

#     # check if input is valid
#         # ! if invalid, get another input from user
#     translation = pigLatin(text_input)
#         # print input and translation
#     print("Input Text: ", text_input, "\nPig Latin Translation: ", translation)

#     # ! send translation
#     # ask if continue translating
#     connected = input("Continue? (y/n): ")

#     # if not, terminate program
#     if(connected == "n" or connected == "no"):
#         connected=False
#         # ! send this to client
#         print("Bye!")