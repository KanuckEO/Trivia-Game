#py
#Kanuck Shah
#Quiz Game

score = 0
yes = (input("Welcome to Tech and Math Trivia. Are you ready to play? (yes/no)"))

if yes == 'yes':
      ans = (input("how many apple Iphones are there"))
      if ans == "20":
            print("Ding Ding Ding!!! you are right")
            score = score + 1
            print("here is your score", score)
            ready1 = (input("next question you ready? (yes is the only answer)"))
            if ready1 == "yes":
                  print("great next question")
                  ans =(input("what is the square root of 1"))
            if ans == '1':
                  print("Ding Ding right answer!!")
                  print("here is your score", score)
                  time.sleep(10)
                  print("next question")
                  ans = (input("Who is the richest man in modern history"))
                  if ans == 'Jeff Bezos':
                        print("Ding, Right answer!")
                        print("here is your score", score)
                  else:
                        print("Sorry wrong answer")
                        print("here is your score", score) 
            else:
                  print("sorry wrong answer")
                  print("here is your score", score)
                  time.sleep(10)
                  print("next question")
                  ans = (input("Who is the richest man in modern history"))
                  if ans == 'Jeff Bezos':
                        print("Ding, Right answer!")
                        print("here is your score", score)
                  else:
                        print("Sorry wrong answer")
                        print("here is your score", score) 
      else: #barrier from first if statment
            print("Sorry wrong answer")
            print("here is your score", score)
            ready1 = (input("next question you ready? (yes is the only answer)"))
            if ready1 == "yes":
                  print("great next question")
                  ans =(input("what is the square root of 1"))
            if ans == '1':
                  print("Ding Ding right answer!!")
                  print("here is your score", score)
                  time.sleep(10)
                  print("next question")
                  ans = (input("Who is the richest man in modern history"))
                  if ans == 'Jeff Bezos':
                        print("Ding, Right answer!")
                        print("here is your score", score)
                  else:
                        print("Sorry wrong answer")
                        print("here is your score", score) 
            else:
                  print("sorry wrong answer")
                  print("here is your score", score)
                  time.sleep(10)
                  print("next question")
                  ans =(input("Who is the richest man in modern history (Has to be upper case letters for start of name and surename)"))
                  if ans == 'Jeff Bezos':
                        print("Ding, Right answer!")
                        print("here is your score", score)
                  else:
                        print("Sorry wrong answer")
                        print("here is your score", score)


                        
