questions=["What is your name?","Where are you from?",
"Who was the founder of pak?","Title of Mashriq Poet given to?",
"Title of Saifullah given to?"]
print("   *** Welcome To Kon Bana Ga Karorpati Show***")
correct_answer=0
a=input(questions[0])
print("Name :",a.capitalize())
b=input(questions[1])
print("City :",b.capitalize())
c=input(questions[2])
print("Ans :",c.capitalize())
if(c=="quaid-e-azam"):
    print("Correct Answer")
    correct_answer1=correct_answer + 1
else:
    print("Wrong Answer")
    print("Correct Ans : quaid-e-azam")
    correct_answer1=correct_answer + 0

d=input(questions[3])
print("Ans :",d.capitalize())
if(d=="allama iqbal"):
    print("Correct Answer")
    correct_answer2=correct_answer1 + 1
else:
    print("Wrong Answer")
    print("Correct ans : allama iqbal")
    correct_answer2=correct_answer1 + 0
e=input(questions[4])
print("Ans :",e.capitalize())
if(e=="khalid bin walid"):
    print("Correct Answer")
    correct_answer3=correct_answer2 + 1
else:
    print("Wrong Answer")
    print("Correct Ans : khalid bin walid")
    correct_answer3=correct_answer2 + 0
if(correct_answer3>=2):
    print("Congratulations! you are winner of Kon Bana Ga Karorpati")
    print("      Name :",a)
    print("      City :",b)
    print("      Your score :",correct_answer3)
    print("      Prize won :1 million dollar")
else:
    print("Best of Luck next time")
    print("      Your score : correct_answer3")
