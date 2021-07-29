"""
Filename: year 11 quiz 
Author: Liam howden
Date: 6/7/2021
Description: this is a year 11 digital tech quiz 
"""
#lists 
questions =["What is a list used for?","what does a print statement do?",
            ]
answers =["A list is used for storing items","prints statements",
          ]
#asking the user for thier name 
print("hello welcome to my year 11 digital quiz!") 
name=input("please enter your name:")
print ("hello" " "+ name )

#asking to start the quiz 
start=input("shall we start the quiz?:" " " + name)
#while start == "no" or start == "n":
if start == "yes" or start == "y" or start =="Yes" or start=="Y" or start=="yeah":
    print("ok cool lets start the quiz" " " + name)
elif start =="no" or start == "n":
    print("okay then umm.........")
    exit()
else:
    exit()   

#the frist two questions 
question_one=input(questions[0])
if question_one ==(answers[0]) or question_one == "storing items" or question_one == "storing multiple items" or question_one == "for storing items"  :
  print("right!")
elif question_one !=(answers[0]) or question_one != "storing items":
    print("sorry thats worng this is the answer" " " + answers[0])
else:
    print ("wrong here is the answer " + answers[0])

question_2=input(questions[1])
if question_2 ==(answers[1]) or question_2 == " printing items" or question_2 == "printing statements"  :
  print("right!")
elif question_2 !=(answers[1]) or question_2 != "printing items":
    print("sorry thats worng this is the answer" " " + answers[1])
else:
    print ("wrong here is the answer " + answers[1])

#ask the questions by using a for loop and going through the question list
# for ....  each question in the list
