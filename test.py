from quest import *


counter = 0
input("For start test  press enter ==>")


if question1() == "a":
    counter += 1
if question2() == "c":
    counter += 1
if question3() == "b":
    counter += 1
if question4() == "b":
    counter += 1
if question5() == "c":
    counter += 1
if question6() == "b":
    counter += 1
if question7() == "a":
    counter += 1
if question8() == "b":
    counter += 1
if question9() == "a":
    counter += 1
if question91() == "b":
    counter += 1
if question92() == "c":
    counter += 1
if question93() == "b":
    counter += 1
 
print("Ви набрали ==== ", counter, "балів")

if counter == 12 or counter == 11 or counter == 10:
    perfectly()
elif counter == 9 or counter == 8 or counter == 7:
    fine()
elif counter == 6 or counter == 5 or counter == 4:
    satisfactorily()
elif counter <= 3:
    unsatisfactory()
