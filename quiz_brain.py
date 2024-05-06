class QuizBrain:
  """The QuizBrain class is responsible for how the entire quiz game works."""
  def __init__(self, q_list:list) -> None:
    self.question_number = 0
    self.question_list = q_list
    self.score = 0

  def next_question(self) -> None:
    """Asks the next question."""
    current_question = self.question_list[self.question_number]
    true_or_false = "(True/False)?"
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} {true_or_false}: ")
    self.check_answer(user_answer, current_question.answer)
  
  def still_has_questions(self) -> bool:
    """Checks if question_list has anymore questions."""
    return len(self.question_list) > self.question_number

  def check_answer(self, user_answer: str, correct_answer: str):
    """Checking if user has said the right answer to give them a score, if they have not answered true or false we take them back to next_question method."""
    the_answer = user_answer[0].upper() + user_answer[1:].lower()
    if the_answer == "True" or the_answer == "False":
      if the_answer == correct_answer:
        self.score += 1
        print("You got it right!")
      else:
        print("That's wrong.")
      print(f"The correct answer was: {correct_answer}")
      print(f"The current score is: {self.score}/{self.question_number}.")
      print()
    else:
      self.question_number -= 1
      self.next_question()
      