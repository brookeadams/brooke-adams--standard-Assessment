#score count start
score = 0
#introduction\say hi and ask name\tell current score - brooke - 02\22 - 0.3
name = input("Kia Ora, what is your name? ")
print("Kia Ora", name + "!")


def q1():
    global score

    print("lets start! question one.")
    #question one of five\tell current score - brooke - 26\05\22 - 0.3
    ans1 = input(
        "what does aporo mean? \na. apple \nb. ants \nc. android \nAnswer: ")
    if ans1 == "a" or ans1 == "apple" or ans1 == "A":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q2()

    elif ans1 == "b" or ans1 == "B" or ans1 == "c" or ans1 == "C" or ans1 == "ants" or ans1 == "android":
        print("wrong!!!")
        q2()
    else:
        print("thats not an option? your current score is", score)
        q2()


def q2():
    global score

    print("are you ready for question 2!")
    #question two of five\tell current score - brooke - 26\05\22 - 0.3
    ans2 = input(
        "what is the number 7 in maori? \na. whitu tekau \nb. whitu \nc. tekau ma whitu \nanswer:"
    )
    if ans2 == "b" or ans2 == "whitu" or ans2 == "B":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q3()

    elif ans2 == "a" or ans2 == "A" or ans2 == "c" or ans2 == "C" or ans2 == "whitu tekau" or ans2 == "tekau ma whitu":
        print("wrong!!!")
        q3()
    else:
        print("thats not an option? next question!!")
        q3()


def q3():
    global score

    #question three of five\tell current score - brooke - 26\05\22 - 0.3
    ans3 = input(
        "what does haikura mean? \na. middle school \nb. high school \nc. pre-school \nAnswer: "
    )
    if ans3 == "b" or ans3 == "high school" or ans3 == "B":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q4()

    elif ans3 == "a" or ans3 == "A" or ans3 == "c" or ans3 == "C" or ans3 == "middle school" or ans3 == "pre-school":
        print("wrong!!!")
        q4()
    else:
        print("thats not an option? next question!!")
        print("your current score is", score)
        q4()


def q4():
    global score

    #question four of five\tell current score - brooke - 26\05\22 - 0.3
    ans4 = input(
        "what emotion is hakoakoa? \na. sadness \nb. anger \nc. happiness \nAnswer: "
    )
    if ans4 == "c" or ans4 == "happiness" or ans4 == "C":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q5()

    elif ans4 == "b" or ans4 == "B" or ans4 == "a" or ans4 == "A" or ans4 == "sadness" or ans4 == "anger":
        print("wrong!!!")
        q5()
    else:
        print("thats not an option? next question!!")
        print("your current score is", score)
        q5()


def q5():
    global score

    #question five of five\tell current score - brooke - 26\05\22 - 0.3
    print("last one!!")

    ans5 = input("what color are bananas? \na. kowhai \nb. papura \nAnswer: ")
    if ans5 == "a" or ans5 == "kowhai" or ans5 == "A" or ans5 == "yellow":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q6()

    elif ans5 == "b" or ans5 == "B" or ans5 == "papura" or ans5 == "purple":
        print("purple banana?? um no your wrong!!!")
        q6()
    else:
        print("thats not an option? your done!your score is",
              score)
        q6()


def q6():
    global score

    #question number six\tell current score - brooke - 02\06\22 - 0.3
    print("quesion 6!!")

    ans6 = input(
        "what is Aotearoa? \na. new zealand \nb. austraila \nc. china \nAnswer: "
    )
    if ans6 == "a" or ans6 == "new zealand" or ans6 == "A":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q7()

    elif ans6 == "b" or ans6 == "B" or ans6 == "china" or ans6 == "austraila" or ans6 == "c" or ans6 == "C":
        print("wrong!?")
        q7()
    else:
        print("thats not an option? your done!")
        q7()
def q7():
    global score

    #question number seven\tell current score - brooke - 06\06\22 - 0.1
    print("next quesion!")

    ans7 = input(
        "In winter it is...? \na. pumahu \nb. kuiki \nc. ngawha \nAnswer: ")
    if ans7 == "b" or ans7 == "kuiki" or ans7 == "B":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q8()

    elif ans7 == "c" or ans7 == "C" or ans7 == "pumahu" or ans7 == "ngawha" or ans7 == "a" or ans7 == "A":
        print("wrong!?")
        q8()
    else:
        print("thats not an option? your done!")
        q8()


def q8():
    global score

    #question number eight\tell current score - brooke - 09\06\22 - 0.2
    print("quesion 8!!")

    ans8 = input(
        "right now i am doing a pataitaitanga, pataitaitanga means? \na. game \nb. quiz \nc. drawing \nAnswer: "
    )
    if ans8 == "b" or ans8 == "kuiki" or ans8 == "B":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q9()

    elif ans8 == "c" or ans8 == "C" or ans8 == "game" or ans8 == "drawing" or ans8 == "a" or ans8 == "A":
        print("wrong!?")
        q9()
    else:
        print("thats not an option? your done!")
        q9()
def q9():
    global score

    #question number nine\tell current score - brooke - 09\06\22 - 0.1
    print("quesion 9!!")

    ans9 = input(
        "what are the two offical languages in nz? \na. english\maori \nb. maori\sign language \nc. english\sign language \nAnswer: "
    )
    if ans9 == "b" or ans9 == "maori\sign language" or ans9 == "B":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q10()

    elif ans9 == "c" or ans9 == "C" or ans9 == "english\maori" or ans9 == "english\sign language" or ans9 == "a" or ans9 == "A":
        print("wrong!?")
        q10()
    else:
        print("thats not an option? your done!")
        q10()

def q10():
    global score

    #question number ten\tell current score - brooke - 09\06\22 - 0.1
    print("quesion 10!!")

    ans10 = input(
        "what does kura mahita mean \na. caretaker \nb. school teacher \nc. dance instructor \nAnswer: "
    )
    if ans10 == "b" or ans10 == "school teacher" or ans10 == "B":
        print("correct!!")
        score = score + 10
        print("your current score is", score)
        q10()

    elif ans10 == "c" or ans10 == "C" or ans10 == "caretaker" or ans10 == "dance instructor" or ans10 == "a" or ans10 == "A":
        print("wrong!?")
        q10()
    else:
        print("thats not an option? your done!")
        q10()
q1()
