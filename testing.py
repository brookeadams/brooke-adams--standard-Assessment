#score count start
score = 0
#introduction\say hi and ask name\tell current score - brooke - 02\22 - 0.3
name = input("Kia Ora, what is your name? ")
print ("Kia Ora", name+ "!")
def q1():
  global score

  
  print("lets start! question one.")
  #question one of five\tell current score - brooke - 02\22 - 0.3
  ans1 = input ("what does aporo mean? \na. apple \nb. ants \nc. android \nAnswer: ")
  if ans1 == "a" or ans1 == "apple" or ans1 == "A" : 
    print("correct!!")
    score = score + 10
    print("your current score is",score)
    q2()
    
  
  elif ans1 == "b" or ans1 == "B" or ans1 == "c" or ans1 == "C" or ans1 == "ants" or ans1 == "android":
    print ("wrong!!!")
    q2()
  else:
    print ("thats not an option?")


def q2():
  global score
  
  print("are you ready for question 2!")
  #question two of five\tell current score - brooke - 02\22 - 0.3
  ans2 = input ("what is the number 7 in maori? \na. whitu tekau \nb. whitu \nc. tekau ma whitu \nanswer:")
  if ans2 == "b" or ans2 == "whitu" or ans2 == "B" : 
    print("correct!!")
    score = score + 10
    print("your current score is",score)
    q3()
    
  
  elif ans2 == "a" or ans2 == "A" or ans2 == "c" or ans2 == "C" or ans2 == "whitu tekau" or ans2 == "tekau ma whitu":
    print ("wrong!!!")
    q3()
  else:
    print ("thats not an option? next question!!")
    q3()






def q3():
  global score
  
  #question three of five\tell current score - brooke - 02\22 - 0.3
  ans3 = input ("what does haikura mean? \na. middle school \nb. high school \nc. pre-school \nAnswer: ")
  if ans3 == "b" or ans3 == "high school" or ans3 == "B" : 
    print("correct!!")
    score = score + 10
    print("your current score is",score)
    q4()
    
  
  elif ans3 == "a" or ans3 == "A" or ans3 == "c" or ans3 == "C" or ans3 == "middle school" or ans3 == "pre-school":
    print ("wrong!!!")
    q4()
  else:
    print ("thats not an option? next question!!")
    print("your current score is",score)
    q4()

def q4():
  global score
  
  #question four of five\tell current score - brooke - 02\22 - 0.3
  ans4= input ("what emotion is hakoakoa? \na. sadness \nb. anger \nc. happiness \nAnswer: ")
  if ans4 == "c" or ans4 == "happiness" or ans4 == "C" : 
    print("correct!!")
    score = score + 10
    print("your current score is",score)
    q5()
    
  
  elif ans4 == "b" or ans4 == "B" or ans4 == "a" or ans4 == "A" or ans4 == "sadness" or ans4 == "anger":
    print ("wrong!!!")
    q5()
  else:
    print ("thats not an option? next question!!")
    print("your current score is",score)
    q5()

def q5():
  global score
  
  #question five of five\tell current score - brooke - 02\22 - 0.3
  print("last one!!")

  ans5 = input ("what color are bananas? \na. kowhai \nb. papura \nAnswer: ")
  if ans5 == "a" or ans5 == "kowhai" or ans5 == "A" or ans5 == "yellow":
    print("correct!!")
    score = score + 10
    print("your current score is",score)
    q6()
    
  
  elif ans5 == "b" or ans5 == "B" or ans5 == "papura" or ans5 == "purple":
   print ("purple banana?? um no your wrong!!!")
   q6()
  else:
    print ("thats not an option? your done!congrats on getting a score of", score)
    q6()

def q6():
  global score
  
  #question number six\tell current score - brooke - 02\22 - 0.3
  print ("quesion 6!!")

  ans6 = input ("what is Aotearoa? \na. new zealand \nb. austraila \nc. china \nAnswer: ")
  if ans6 == "a" or ans6 == "new zealand" or ans6 == "A":
    print("correct!!")
    score = score + 10
    print("your current score is",score)
    q6()
    
  
  elif ans6 == "b" or ans6 == "B" or ans6 == "china" or ans6 == "austraila" or ans6 == "c" or ans6 == "C":
   print ("wrong!?")
   q6()
  else:
    print ("thats not an option? your done!")
    q6()

q1()