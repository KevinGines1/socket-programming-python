import socket
#* ========================================= FUNCTIONS

# function that sets up the server
def setupServer():

    # create a socket object with IPv6 & TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        #use port 5000
        host = '' # this is blank so we can accept connections from other computers
        port = 5000
        s.bind((host, port)) # bind the port 5000 and host to the socket
        
        print("Socket successfully created")
        print("Socket binded to ", port)
        
        s.listen() # wait for computers to connect
        
        print("socket is listening")
        return s
    
    except socket.error as msg:
        print("Bind failed. Error Code: ", str(msg[0]), " Message: ", msg[1])

# function that converts a list of strings to pigLatin
def pigLatin(text):
    deconstruct = [] # a list of words when the input text is a sentence/phrase/ more than one word delimited by spaces
    translated = "" # holder for the translated word
    if " " in text: # if the input is a sentence
        deconstruct = text.split(" ")

        for word in deconstruct: # translate each word to piglatin
            translated = translated + pigLatinHelper(word)
            translated = translated + " "

    else: # if there is only one word in the input
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

    translation = text

    conso_clust = "" # consonant cluster

    # if first letter is a consonant
    if text[0] not in ["a", "e", "i", "o", "u"]:
        if isAllConsonant(text): # if all letters in the word is a consonant (e.g. my, rhythms)
            translation = translation[len(translation)-1] + translation[0:len(translation)-1] # we only get the consonant cluster up until the second to the last
            translation = translation + "ay"
        else: # otherwise
            for letter in text:
                if letter not in ["a", "e", "i", "o", "u"]: # collect the cluster
                    conso_clust = conso_clust + letter
                    
                    translation = translation[1:len(translation)]
                else: # when a vowel is encountered
                    translation = translation + conso_clust
                    translation = translation + "ay"
                    break
    else: # if the first letter is a vowel, we simply add yay at the end
        translation = translation + "yay"
    

    return translation
#* ===================================================

s = setupServer()

#prompt messages to be sent
message = "Successfully connected to the server"
prompt = "What do you want to translate to Pig Latin? : "
cont = "Continue? (y/n): "


while True:
    
    c, addr = s.accept() # establish connection with a client
    print("Got connection from ", addr)
    c.send(message.encode()) #acknowledge client of the connection

    proceed = "y"
    while proceed != "n":
        c.send(prompt.encode()) # please enter a word
        input_text = c.recv(1024) # wait for an input
        input_text = input_text.decode() # decode received input
        print("Input: ", input_text)

        trans_text = pigLatin(input_text)
        print("Output: ", trans_text)
        
        c.send(trans_text.encode()) # send translated word to client
        c.send(cont.encode()) # send continue? prompt
        proceed = c.recv(1024).decode()

c.close()