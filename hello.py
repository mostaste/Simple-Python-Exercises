# This program says hello and asks for my name
import time

nameAI = 'Alice'

def typeLetters(str):
    for letter in str:
        print(letter, end = '')
        time.sleep(.05)


# TODO Input Error Checking TRY EXCEPT
# Right Justify
print(nameAI, end = ':  ') 
typeLetters('Hello, What is your name?\n')
myName = str(input())
print(nameAI, end = ':  ')
typeLetters('It is good to meet you, ' + myName + '\n')
lenOfName = len(myName)
print(nameAI, end = ':  ')
typeLetters('What is your age?\n')
print(myName, end = ':  ')
myAge = int(input())
print(nameAI, end = ':  ')
typeLetters('You are ' + str(myAge) + ' years old')

