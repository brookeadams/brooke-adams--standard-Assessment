def q1():

  print("lets start! question one.")
  #question one of five\tell current score - brooke - 02\22 - 0.3
  ans1 = input ("what does aporo mean? \na. apple \nb. ants \nc. android \nAnswer: ")
  if ans1 == "a" or ans1 == "apple" or ans1 == "A" : 
    print("correct!!")
    #score = score + 10
    q2()
  
  
  elif ans1 == "b" or ans1 == "B" or ans1 == "c" or ans1 == "C" or ans1 == "ants" or ans1 == "android":
    print ("wrong!!!")
    q2()
  else:
    print ("thats not an option?")


def q2():

  print("lets start! question one.")
  #question one of five\tell current score - brooke - 02\22 - 0.3
  ans1 = input ("what does aporo mean? \na. apple \nb. ants \nc. android \nAnswer: ")
  if ans1 == "a" or ans1 == "apple" or ans1 == "A" : 
    print("correct!!")
    #score = score + 10
  
  
  elif ans1 == "b" or ans1 == "B" or ans1 == "c" or ans1 == "C" or ans1 == "ants" or ans1 == "android":
    print ("wrong!!!")
  else:
    print ("thats not an option?")

q1()



global score