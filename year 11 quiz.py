"""
Date: 6/7/2021
Description: this is a year 11 digital tech quiz 
"""
print(" try not to put a space at the start of an answer\n  \n")
#ponits       
user_points =0

#lists 
questions =["What is a list used for?:","what does a print statement do?:","What can you use to loop your code?(hint) put loop at the end:","how do you end a if statement?(hint with what key):","what key do you press to make a comment"
            ,"what verson of python are we using now?","what opens when you test your code?(hint on a school verson of python):","what is the name of the language we are using?","who made python(hint only need fristname):","when was python made?(hint its near the end of the 1900):"
            ]
answers =["A list is used for storing items","prints statements","while loop",":","#","3.9.5","pyhton shell","python","Guido","1991"
          ]
#asking the user for their name 
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
   are_you_sure=input("are you sure you want to exit the quiz before it starts?")
   if are_you_sure =="yes" or are_you_sure =="y" or are_you_sure == "Y" or are_you_sure == "Yes" or are_you_sure =="yeah":
       exit()   
   elif are_you_sure =="no" or are_you_sure =="n" or are_you_sure == "N" or are_you_sure == "No":
    print("ok cool")

#the first two questions
# for each question in the list.  First print out the question and get an answer from the user
# then compare the user answer to what the actual answer is in the answers list and print out
# a message according to whether or not they got it right.


print(" ")
question_one=input(questions[0])
if question_one ==(answers[0]) or question_one == "storing items" or question_one == "storing multiple items" or question_one == "for storing items"  :
  print("right!")
  user_points +=1
elif question_one !=(answers[0]) or question_one != "storing items":
    print("sorry thats wrong this is the answer" " " + answers[0])
else:
    print ("wrong here is the answer " + answers[0])

# i have made gaps between the qustions in this version as it makes it easyer to know what question is what (for me at least) 

print(" ")
question_2=input(questions[1])
if question_2 ==(answers[1]) or question_2 == " printing items" or question_2 == "printing statements"  :
  print("goodwork!")
  user_points +=1
elif question_2 !=(answers[1]) or question_2 != "printing items":
    print("sorry thats wrong this is the answer" " " + answers[1])
else:
    print ("wrong here is the answer " + answers[1])



print(" ")
#trial 2 won the trail votes and so i will use this type of code to make a looping system 
correct = False
while not correct:
    question_3=input(questions[2])
    if question_3 ==(answers[2]) or question_3 == "While loop" or question_3 == "for loop"  :
            print("rightyo!")
            correct = True
            user_points +=1

    elif question_3 !=(answers[1]) or question_3 != "printing items":
        print("sorry thats wrong this is the answer" " " )


print(" ")
#question 4 there is no more loop as qustion 3 was the "break" question if you will qustion 6 will also have a loop
question_4=input(questions[3])
if question_one ==(answers[3]) or question_4 == "colon":
  print("yooooooo you got it!!!")
  user_points +=1
elif question_4 !=(answers[3]) or question_4 != "colon":
    print("sorry thats wrong this is the answer" " " + answers[3])
else:
    print ("wrong here is the answer " + answers[3])


print(" ")
#this question is some what hard like qustion 4
question_5=input(questions[4])
if question_one ==(answers[4]) or question_5 == "hashtag":
  print("YES!")
  user_points +=1
elif question_5 !=(answers[4]) or question_5 != "hashtag":
    print("sorry thats wrong this is the answer" " " + answers[4])
else:
    print ("wrong here is the answer " + answers[4])



print(" ")
#looping again as it is question 6(NOTE this code was made using the python verson 3.9.5 so if you are using this in the future please update it unless i do many thanks)
correct = False
while not correct:
    question_6=input(questions[5])
    if question_6 ==(answers[5]) or question_6 == "3.9.4"  :
            print("you got it right!")
            correct = True
            user_points +=1

    elif question_6 !=(answers[1]) or question_6 != "3.9.4":
        print("sorry thats wrong this is the answer" " " )



print(" " )
# just more questions not anything to exciting 
question_7=input(questions[6])
if question_one ==(answers[6]) or question_7 == "shell":
  print("yay you got it but if you did'nt i would be mad")
  user_points +=1
elif question_7 !=(answers[6])or question_7 == "shell":
    print("HOW DID YOU GET IT WRONG?!?!??!" " " + answers[6])
else:
    print ("HOW!?!?!??  " + answers[6])



print(" ")
question_8=input(questions[7])
if question_one ==(answers[7]) or question_8 == "python":
  print("LETS GOOOO!!!!!")
  user_points +=1
elif question_8 !=(answers[7]) or question_8 == "python":
    print("thats wrong" " " + answers[7])
else:
    print ("sorry thats wrong " + answers[7])


#this qustion i am using a print statement before the question starts to ask the people not to use google on the next two questions
#and in this version i have got rid of the mutliple print(" ") as the space was to large

print(" ")
print("this qustions are a lot harder to anwser but please dont google them thanks")

question_9=input(questions[8])
if question_9 ==(answers[8])   :
  print("great arnt you gald it was only the frist name!")
  user_points +=1
elif question_9 !=(answers[8]):
    print("sorry thats not right but at least you did'nt use google as you did'nt know this is his name!" " " + answers[8])
else:
    print ("wrong here is the answer " + answers[8])



print(" ")
question_10=input(questions[9])
if question_10 ==(answers[9])   :
  print("greatwork you got it right!")
  user_points +=1
elif question_10 !=(answers[9]):
    print("well you did your best " " " + answers[9])
else:
    print ("wrong here is the answer " + answers[9])



print(" ")
print(" ")

print("THANK YOU FOR PLAYING -by liam howden!")

#to show the user their score
print("your score is out of 10")
print(user_points)


#that is all i have done for this quiz thank you for reading my code and playing the quiz if you did play it many thanks liam howden 




