#Visual Studio Codes:

#print ("Moikka!")
#name=input("What is your name? yes/no")
#print (f"Hello,{name}!")

#def sade_aktiviteetit():
    #rain=input("Is it raining? ")
    #print (f"{rain}")
    #if rain=="yes":
    # print("Go to movies")
    #elif rain=="no":
        #print("Go to picnic")
    #else:
        #print("It's hard to tell nowadays")
#sade_aktiviteetit

#foods=["pizza","pasta","vegetables","meet","fish"]
#for food in foods:
    #print("I like",food)
'''
price=int(input("what's the price of your meal? "))
print (f"Price is {price}")
tax=price*0.1
tip=price*0.05
print("Total is ", price + tax + tip)


def calculate_total(original_price):
    return original_price + original_price*0.24 + original_price*0.05
hamburger_price=float(input("Price of hamburger? "))
hamburger_total_price=calculate_total(hamburger_price)
print("Total is ",hamburger_total_price)
'''
'''
#Tämä ohje oli netissä: Python Encoding
string = input("Enter a string\n")
string= str.upper(string)
for x in string:
    if(x==' '):
        print(' ',end='')
    elif(ord(x)-ord('A')+3 >= 26 ):
        print(chr(ord(x)-26+3), end='')
    else:
        print (chr(ord(x)+3), end='')
'''
'''
#näin tehtiin kurssilla:
#viestin avaaminen miinustamalla
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','å','ä','ö',' ']
message=input("Kerro viestisi? ").lower()
encrypted=""
for letter in message:
    letter_index = alphabet.index(letter)
    new_letter_index=letter_index + 3
    if new_letter_index >= len(alphabet):
        new_letter_index = new_letter_index - len(alphabet)
    encrypted=encrypted + alphabet[new_letter_index]
print(encrypted)
'''
'''
import random
adjectives=["kaunis","ruma","luminen","talvinen"]
subjectives=["kissa","koira","auto","ihminen"]
characters=["9", "?", "@","*"]

def create_password():
    my_random_subjectives=random.choice(subjectives)
    my_random_adjectives=random.choice(adjectives)
    my_random_characters=random.choice(characters)
    new_password=random.choice(adjectives) + random.choice(subjectives) + random.choice(characters)
    return new_password
print(create_password())
'''
import os
import datetime

file_path='C:/Users/oma/Desktop/diary.txt'

if not os.path.exists(file_path):
        print("Onko tämä oikea paikka?", file_path)

with open(file_path,"a") as diary:
    aihe=input("Mikä on päivän aihe? ")
    teksti=input("Mikä on päivän teksti? ")
        #diary.writelines("Moi!")
    date=datetime.datetime.now()
    pretty_date=f"{date.day}.{date.month}.{date.year}"
    diary.writelines(f"Date: {pretty_date} {os.linesep}Topic: {aihe}{os.linesep}")
    diary.writelines(teksti)
    diary.writelines(f"{os.linesep}********{os.linesep}")
    
#Turtle-koodit
import turtle
import random

franklin=turtle.Turtle()
franklin.color("Olive Drab")
'''
franklin.pensize(10)
franklin.shape ("turtle")
'''
'''
def draw_square(width,color):
    franklin.color("Olive Drab")
    for x in range (4):
        franklin.forward(width)
        franklin.left(90)
draw_square (150,"Olive Drab")
'''
'''
def draw_triangle (width,color):
        franklin.fillcolor(color)
        franklin.begin_fill()       
        for x in range (3):
            franklin.forward(width)
            franklin.left(120)
        franklin.end_fill()  
draw_triangle (150,"Olive Drab")
'''
colors=["red","blue","green","hotpink","black","Olive Drab"]
'''
for x in range (300):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    random_color=random.choice(colors)
    franklin.penup()
    franklin.goto(x,y)
    franklin.pendown()
    franklin.fillcolor(random_color)
    franklin.begin_fill()
    franklin.circle(20)
    franklin.end_fill()
    franklin.speed(0)
'''
'''
def draw_circle(t, sz):
  for i in range(4):
    t.forward(sz)
    t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightblue")
for i in range(1,24):
  draw_circle(franklin,100)
  franklin.left(18)
'''


for x in range(360):
    franklin.pencolor(colors[x % 6])
    franklin.width(x / 100 + 1)
    franklin.forward(x)
    franklin.left(59)
    franklin.circle(80)
    
    
    
#Replit Python Hangman
Variables and function definitions below:
'''
import random
words = ["tuoli","poyta","matto"]
correct_word=random.choice(words)
clue=["?","?","?","?","?"]
lives=7

'''
Start executing your code below:
'''
while True:
  print(clue)
  kirjain=input("Arvaa kirjain? ")

  if kirjain in correct_word:
    for i in range(len(correct_word)):
      if correct_word[i]==kirjain:
        clue[i]=kirjain
  else:
    lives=lives-1
  if lives==0:
     print("That's that then")
     break
  if not "?" in clue:
    print("You're the winner!")
    break
 
 #Replit Python Hangman
 
Variables and function definitions below:
'''
import random
words = ["tuoli","poyta","matto"]
correct_word=random.choice(words)
clue=["?","?","?","?","?"]
lives=7

'''
Start executing your code below:
'''
while True:
  print(clue)
  kirjain=input("Arvaa kirjain? ")

  if kirjain in correct_word:
    for i in range(len(correct_word)):
      if correct_word[i]==kirjain:
        clue[i]=kirjain
  else:
    lives=lives-1
  if lives==0:
     print("That's that then")
     break
  if not "?" in clue:
    print("You're the winner!")
    break
