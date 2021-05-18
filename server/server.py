


# ! establish connection
connected = True

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

def isAllConsonant(text):
    for letter in text:
        if letter in ["a", "e", "i", "o", "u"]:
            return False
    return True

#function that converts input text to piglatin
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

while(connected):
    # get input from client
    text_input = input()

    # check if input is valid
    # if not (text_input.isalpha()):
        # print("invalid input!")
        # ! if invalid, get another input from user
        # return dapat or ask for another input from the user
    # else: 
        # if valid, convert input to pig latin
    translation = pigLatin(text_input)
        # print input and translation
    print("Input Text: ", text_input, "\nPig Latin Translation: ", translation)

    # ! send translation
    # ask if continue translating
    connected = input("Continue? (y/n): ")

    # if not, terminate program
    if(connected == "n" or connected == "no"):
        connected=False
        # ! send this to client
        print("Bye!")