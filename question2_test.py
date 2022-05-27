print("are you ready for question 2!")

ans2 = input ("what is the number 7 in maori? \na. whitu tekau \nb. whitu \nc. tekau ma whitu \nanswer:")
if ans2 == "b" or ans2 == "whitu" or ans2 == "B" : 
  print("correct !!")

elif ans2 == "a" or ans2 == "A" or ans2 == "c" or ans2 == "C" or ans2 == "whitu tekau" or ans2 == "tekau ma whitu":
  print ("wrong!!!")
else:
  print ("thats not an option? next question!!")