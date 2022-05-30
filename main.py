score = 0

name = input("Kia Ora, what is your name? ")
print ("Kia Ora", name+ "!")

instructions = input("would you like the instructions on this quiz?")
instructions = instructions.lower()
if instructions == " yes":
  print("to add points to your score you must get the quesions correct but if you get them incorrect the score will stay the same!")

elif instructions == " no":
  print("ok then")

print("lets start! question one.")

ans1 = input ("what does aporo mean? \na. apple \nb. ants \nc. android \nAnswer: ")
if ans1 == "a" or ans1 == "apple" or ans1 == "A" : 
  print("correct!!")

elif ans1 == "b" or ans1 == "B" or ans1 == "c" or ans1 == "C" or ans1 == "ants" or ans1 == "android":
  print ("wrong!!!")
else:
  print ("thats not an option? your current score is" + score) 

print("are you ready for question 2!")

ans2 = input ("what is the number 7 in maori? \na. whitu tekau \nb. whitu \nc. tekau ma whitu \nanswer:")
if ans2 == "b" or ans2 == "whitu" or ans2 == "B" : 
  print("correct !!")

elif ans2 == "a" or ans2 == "A" or ans2 == "c" or ans2 == "C" or ans2 == "whitu tekau" or ans2 == "tekau ma whitu":
  print ("wrong!!!")
else:
  print ("thats not an option? next question!!")

ans3 = input ("what does kura tuarua mean? \na. middle school \nb. high school \nc. pre-school \nAnswer: ")
if ans3 == "b" or ans3 == "high school" or ans3 == "B" : 
  print("correct!!")

elif ans3 == "a" or ans3 == "A" or ans3 == "c" or ans3 == "C" or ans3 == "middle school" or ans3 == "pre-school":
  print ("wrong!!!")
else:
  print ("thats not an option? next question!!")

print("Next question!")

ans3 = input ("what emotion is harikoa? \na. sadness \nb. anger \nc. happiness \nAnswer: ")
if ans3 == "c" or ans3 == "happiness" or ans3 == "C" : 
  print("correct!!")

elif ans3 == "b" or ans3 == "B" or ans3 == "a" or ans3 == "A" or ans3 == "sadness" or ans3 == "anger":
  print ("wrong!!!")
else:
  print ("thats not an option? next question!!")

print("last one!!")

ans5 = input ("what color are bananas? \na. kowhai \nb. papura \nAnswer: ")
if ans5 == "a" or ans5 == "kowhai" or ans5 == "A" or ans5 == "yellow":
  print("correct!!")

elif ans5 == "b" or ans5 == "B" or ans5 == "papura" or ans5 == "purple":
  print ("purple banana?? um no your wrong!!!")
else:
  print ("thats not an option? your done!")

