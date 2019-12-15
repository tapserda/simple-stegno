from os import system, name
from stegano import lsb

def clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

def createmessage():
   global code
   code = input("Enter your code : ")
   print ("This your message,\n %s." % code)

def yourimageloc():
   global image_loc
   image_loc = input("Enter you image location : ")
   print ("This your image location,\n %s." % image_loc)

def encoding():
   secret = lsb.hide(image_loc, code)
   secret.save("./stegno.png")
   print("Your code has been encode and saved \nstegno.png")

def decoding():
   imagetodecode = input("Where your image location : ")
   decoding_image = lsb.reveal(imagetodecode)
   print("There your code :\n")
   print(decoding_image)

choice = False
while choice is not True:
   lilchoice = input("\n1 - Encode your code to image \n2 - Decode your code \n3 - Exit \n")
   if lilchoice == '1':
      choice=False
      clear()
      createmessage()
      yourimageloc()
      encoding()
   elif lilchoice == '2':
      choice=False
      clear()
      decoding()
   elif lilchoice == '3':
      choice=True
      print("See yaa later..")
      exit()
   else:
      choice=False
      print("Wrong Number!")
