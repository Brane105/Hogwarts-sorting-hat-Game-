print("""
  __                                       __   __
 | |__   __ _ _ __ _ __ _   _   _ __   ___ | |_| |_ ___ _ __ 
 | '_ \ / _` | '__| '__| | | | | '_ \ / _ \| __| __/ _ \ '__|
 | | | | (_| | |  | |  | |_| | | |_) | (_) | |_| ||  __/ |   
 |_| |_|\__,_|_|  |_|   \__, | | .__/ \___/ \__|\__\___|_|   
                        |___/  |_|                           """)

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
#question 1 
q1_answer = input("Q1.How would you describe yourself?\na)brave\nb)studious\nc)loyal\nd)ambitious? \n ans = ")
if q1_answer == "a":
  gryffindor += 1
elif q1_answer == "b":
  ravenclaw += 1
elif q1_answer == "c":
  hufflepuff += 1
elif q1_answer == "d":
  slytherin += 1
else:
  print("Sorry, I don't understand that answer.")
#question 2 
q2_answer = input("Q2.What can you be found doing on the weekends? \na) Going on adventures \nb) Doing my homework \nc) Spending time with family or friends \nd) Plotting revenge on my enemies\n ans= ")
if q2_answer == 'a':
  gryffindor += 1
elif q2_answer == 'b':
  ravenclaw += 1
elif q2_answer == 'c':
  hufflepuff +=1
elif q2_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")
#question no. 3 
q3_answer = input("Q3.What would you do if the Dark Lord was going to invade your school? \na) Fight him \nb) Look up some good defensive curses in a book \nc) Stand by my friends no matter what \nd) Help the Dark Lord invade the school as an inside spy\n ans= ")
if q3_answer == 'a':
  gryffindor += 1
elif q3_answer == 'b':
  ravenclaw += 1
elif q3_answer == 'c':
  hufflepuff +=1
elif q3_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

#if else statment for the sorting :
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print("GRYFFINDOR!!!!!!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print("RAVENCLAW!!!!!!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
   print("HUFFLEPUFF!!!!!!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print("SLYTHERIN!!!!!!")
else:
  print("Too difficult to decide... Maybe this quiz needs more questions.")