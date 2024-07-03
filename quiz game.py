#-------------------------------
def new_game():
    guesses=[]
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)


        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#-------------------------------
def check_answer(answer,guess):
    if guess == answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#-------------------------------
def display_score(correct_guesses, guesses):
   print("-------------------------------")
   print("Results")
   print("-------------------------------")
   print("Answers: ",end="")
   for i in questions:
       print(questions.get(i),end=" ")
   print()
   print("guesses: ", end="")
   for i in guesses:
      print(i, end =" ")
   print()
   score = int((correct_guesses/len(questions))*100)
   print("Your score is: "+str(score)+"%")
#-------------------------------
def play_again():

    response = input("Would you like to play again? (Y/N): ")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False
#-------------------------------
questions ={
"who created Tekken?: ": "A",
"what year Tekken was launched?: ": "B",
"who is the main character of Tekken 8?: ":"C",
"Do you play Tekken?: ": "A"}

options = [
["A. Harada","B. Happy singh","C. Elonk musk","D. Emperor mishima"],
["A. 1997","B. 1994","C. 1996","D. 1995"],
["A. kazuya mishima","B. Jin kazama","C. King","D. Yoshimitsu"],
["A. Yes","B. No","C. Sometimes","D. What is tekken bro? we play fifa"]
]


new_game()
while play_again():
    new_game()

print("keep calm and do electrics")













