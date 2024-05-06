import requests
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

r = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
res_json = r.json()

question_bank = [Question(dic["text"], dic["answer"]) for dic in question_data]

# TODO: 1. asking questions
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
  answer = quiz.next_question()

print("You've completed the quiz ")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")

if quiz.score / quiz.question_number > 0.7:
  more = input("Would you like to try some harder question? (yes/no): ").lower()
  if more == "yes":
    question_bank = [Question(dic["question"], dic["correct_answer"]) for dic in res_json["results"]]
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
      answer = quiz.next_question()
    
    print("You've completed the quiz ")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
    print()
    print("Good bye.")
  else:
    print("Good bye.")