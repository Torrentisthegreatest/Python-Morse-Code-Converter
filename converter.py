#Setting Directory
morsealpha={ 
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/", 
        "0" : "-----", 
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "." : ".-.-.-",
        "," : "--..--",
        "?" : "..--..",
        "!" : "..--.",
        ":" : "---...",
        "'" : ".---.",
        "=" : "-...-", 
        '"' : ".-..-."
}
#Asking for String
Sen = input("Enter string: ")
#Checking if number is valid
if not Sen.numeric():
  #Making string uppercase to convert
  Sen = Sen.upper()
  #Control loop prints each letter w/ a space in between
  for x in range(len(Sen)) :
    #morsealpha[Sen[x]] prints the xth letter but converted using the Directory
    print(morsealpha[Sen[x]], end="")

else:
  #Telling user the input is Invalid
  print("Invalid input")
  
  
  
