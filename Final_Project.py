import random
uppercaseletter=chr(random.randint(65,90))
lowercaseletter=chr(random.randint(97,122))
symbol=chr(random.randint(33, 47))
number=chr(random.randint(48, 57))

#Shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseletter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseletter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseletter3=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
number1=chr(random.randint(48, 57)) #Generate a random number 0-9 (based on ASCII code)
number2=chr(random.randint(48, 57)) #Generate a random number 0-9(based on ASCII code)
symbol1=chr(random.randint(33, 47)) #Generate a random symbol (based on ASCII code)
symbol2=chr(random.randint(33, 47)) #Generate a random symbol (based on ASCII code)

#Generate password using all the characters in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseletter1 + lowercaseletter2 + lowercaseletter3 + number1 + number2 + symbol1 + symbol2
password = shuffle(password)

#This will save the randomly generated password in a .txt file
with open('passwords.txt', 'a') as f:
  f.write('\n')
  f.write(password)

#Ouput
print(password)