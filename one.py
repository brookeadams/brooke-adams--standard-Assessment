#score count start
score = 0
#introduction\say hi and ask name\tell current score - brooke - 02\22 - 0.3
name = input("Kia Ora, what is your name? ")
print ("Kia Ora", name+ "!")

print("your current score is",score)

print("lets start! question one.")
#question one of five\tell current score - brooke - 02\22 - 0.3
ans1 = input ("what does aporo mean? \na. apple \nb. ants \nc. android \nAnswer: ")
if ans1 == "a" or ans1 == "apple" or ans1 == "A" : 
  print("correct!!")
  score = score + 10


elif ans1 == "b" or ans1 == "B" or ans1 == "c" or ans1 == "C" or ans1 == "ants" or ans1 == "android":
  print ("wrong!!!")
else:
  print ("thats not an option?")
#question two of five\tell current score - brooke - 02\22 - 0.3
print("are you ready for question 2!")

print("your current score is",score)

ans2 = input ("what is the number 7 in maori? \na. whitu tekau \nb. whitu \nc. tekau ma whitu \nanswer:")
if ans2 == "b" or ans2 == "whitu" or ans2 == "B" : 
  print("correct !!")
  score = score + 10

elif ans2 == "a" or ans2 == "A" or ans2 == "c" or ans2 == "C" or ans2 == "whitu tekau" or ans2 == "tekau ma whitu":
  print ("wrong!!!")
else:
  print ("thats not an option? next question!!")
print("your current score is",score)
#question three of five\tell current score - brooke - 02\22 - 0.3
ans3 = input ("what does haikura mean? \na. middle school \nb. high school \nc. pre-school \nAnswer: ")
if ans3 == "b" or ans3 == "high school" or ans3 == "B" : 
  print("correct!!")
  score = score + 10
  
elif ans3 == "a" or ans3 == "A" or ans3 == "c" or ans3 == "C" or ans3 == "middle school" or ans3 == "pre-school":
  print ("wrong!!!")
else:
  print ("thats not an option? next question!!")
print("your current score is",score)
#question four of five\tell current score - brooke - 02\22 - 0.3
print("Next question!")

ans3 = input ("what emotion is hakoakoa? \na. sadness \nb. anger \nc. happiness \nAnswer: ")
if ans3 == "c" or ans3 == "happiness" or ans3 == "C" : 
  print("correct!!")
  score = score + 10

elif ans3 == "b" or ans3 == "B" or ans3 == "a" or ans3 == "A" or ans3 == "sadness" or ans3 == "anger":
  print ("wrong!!!")
else:
  print ("thats not an option? next question!!")
print("your current score is",score)
#question five of five\tell current score - brooke - 02\22 - 0.3
print("last one!!")

ans5 = input ("what color are bananas? \na. kowhai \nb. papura \nAnswer: ")
if ans5 == "a" or ans5 == "kowhai" or ans5 == "A" or ans5 == "yellow":
  print("correct!! congrats on getting a score of", score)
  score = score + 10

elif ans5 == "b" or ans5 == "B" or ans5 == "papura" or ans5 == "purple":
  print ("purple banana?? um no your wrong!!!congrats on getting a score of", score)
else:
  print ("thats not an option? your done!congrats on getting a score of", score)
