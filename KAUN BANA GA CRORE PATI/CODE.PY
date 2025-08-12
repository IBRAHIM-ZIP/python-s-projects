import random                                                 #importing random module to shuffle options
import time                                                 #importing time module to add delays in the game
def options(x):
    global count, score,  xcount,start                      
    a=list_of_answers[x]
    incorrect_answers = random.sample(
        [ans for ans in list_of_answers if ans != a], 3
    )
    y=incorrect_answers+[a]                                # Ensure the correct answer is included in the options
    random.shuffle(y)                                      # Shuffle the options to randomize their order
    print()
    print("Here are your options:")
    for index, option in enumerate(y):
        print(f"                           Option {index + 1}: {option}"       )
        print()
    c = y.index(a)                                           # Get the index of the correct answer.
    
    input_choice =int(input("Please select the correct option (1-4):"))
    if 1<=input_choice<5:
        if input_choice == c+1:
            print("You selected:", y[input_choice - 1])
            print()
            print("✅✅correct answer✅✅")
            score += 10
            start -= 1
            time.sleep(1)
            count+=1
            if start>0:
                print("Your next question is coming up...")
                time.sleep(3)
                return True
            else:
                print("                             Congratulations! You have answered all questions correctly!"                         )
                return False
            
        elif input_choice != c+1:
            print("❌❌Incorrect answer❌❌")
            print("Incorrect answer. The correct answer is:", a)
            xcount+=len(list_of_questions) - start
            start-=1
            time.sleep(1)
            print("You have lost a chance to answer the remaining  question.")
            return False
            
    else:
        print ("please select a valid option (1-4)")




def calculate_score(correct_answers,wrong_answer,  total_questions):
    print("Calculating score...")
    time.sleep(4)
    print("Exited to watch your performace..")
    time.sleep(5)
    print(f"The total Questions are: {total_questions}")
    print(f" Total Correct Answers: {correct_answers}")
    print(f"Your final score is: {correct_answers * 10} out of {total_questions * 10}")
    if correct_answers== total_questions:
        print("🎉🎉🎉🎉🎉Congratulations! You have answered all questions correctly!🎉🎉🎉🎉🎉")
    print()
    print(f"💸💸💸💸💸You have won {correct_answers * 1000000}💸💸💸💸💸")


# List of questions and answers
list_of_questions =[" What is the capital of France?", "What is the largest planet in our solar system?",
                    "Who wrote 'To Kill a Mockingbird'?", "What is the boiling point of water?",
                    "Who painted the Mona Lisa?", "What is the chemical symbol for gold?",
                    "What is the longest river in the world?", "Who discovered penicillin?",
                    "What is the hardest natural substance on Earth?", 
                    "Who was the first person to walon the moon?", "What is the largest mammal in the world?",
                    "What is the smallest country in the world?", "Who invented the telephone?",
                    "Who is the co-founder of Microsoft?", "What is the capital of Japan?",]
list_of_answers = ["Paris", "Jupiter", "Harper Lee", "100 degrees Celsius", "Leonardo da Vinci",
                       "Au", "Nile", "Alexander Fleming", "Diamond", "Neil Armstrong",
                       "Blue Whale", "Vatican City", "Alexander Graham Bell", "Bill Gates",
                       "Tokyo", "Avocado", "Banana", "Apple", "Orange", "Grapes","albert instein",
                       "Isaac Newton", "Galileo Galilei", "Marie Curie", "Nikola Tesla", "Thomas Edison",
                       "Charles Darwin", "Stephen Hawking", "Ada Lovelace", "Alan Turing","india", "USA", "China", "Russia", "Brazil", "Australia", "Canada", "Germany",
                       "France", "Italy", "Spain", "Mexico", "South Africa", "Egypt",
                       "DOLPHIN", "TIGER", "LION", "ELEPHANT", "GIRAFFE", "ZEBRA", "KANGAROO",
                       "Ag", "Hg", "Fe", "Cu", "Pb", "Zn", "Ni", "Al", "Si", "Cl",]
print("\n")
print('💫💫💫💫💫💫💫💫💫💫💫"WELCOME TO KAUN BANA GA CRORE PATI"💫💫💫💫💫💫💫💫💫💫💫')
print("\n")
print("DO YOU WANT TO READ THE RULES OF THE GAME?(IF YES, TYPE 'YES' ELSE TYPE 'NO')")
rules=input("Type your answer here: ").strip().lower()
while rules=="yes":
    print("1. You will be asked 15 questions.")
    print("2. Each question will have 4 options, and you need to select the correct one.")
    print("3. For each correct answer, you will earn 10 points.")
    print("4. If you answer all questions correctly, you will win the game!")
    print("5. If you answer incorrectly, you will lose a chance to answer the next question.")
    print("6. The game ends when you either answer all questions or run out of chances.")
    print("7.THERE IS A CASH PRIZE OF 1,000,000 FOR EACH CORRECT ANSWER!")
    print("7. Good luck!")
    break
else:
    print("You chose not to read the rules. Let's start the game!")
    print("")

score=0
count=0
xcount=0
start=len(list_of_questions)
while True:
    if start>0:
        time.sleep(1)
        print("QUIZ STARTED SOON ...")
        print("Loading....")
        time.sleep(3)
        for index,question in enumerate(list_of_questions):
            print(f"Your score is: {score}")
            print(f"Question {index+1}: {question}")
            x=index
            r=options(x)
            if r is True:
                print()
                
            else:
                print("GAME OVER!")
                calculate_score(count, xcount, len(list_of_questions))
                break
            print("")
        break
         
    else:
        print("Thank you for playing!")