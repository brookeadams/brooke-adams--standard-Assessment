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

print("your current score is",score)

ans2 = input ("what is the number 7 in maori? \na. whitu tekau \nb. whitu \nc. tekau ma whitu \nanswer:")
if ans2 == "b" or ans2 == "whitu" or ans2 == "B" : 
  print("correct !!")
  q2()
  score = score + 10

elif ans2 == "a" or ans2 == "A" or ans2 == "c" or ans2 == "C" or ans2 == "whitu tekau" or ans2 == "tekau ma whitu":
  print ("wrong!!!")
  q2()
else:
  print ("thats not an option? next question!!")
print("your current score is",score)
q2()



q1()



