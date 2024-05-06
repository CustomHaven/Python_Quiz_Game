class Question:
  """Question class stores the question and answers."""
  def __init__(self, text:str, answer:str) -> None:
    self.text = text
    self.answer = answer