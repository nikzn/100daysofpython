from question_model import  Question
from data import question_data,logo
from quiz_brain import QuizBrain

print(logo)

questionBank=[]
for question in question_data:
    newQuestion = Question(question["text"],question["answer"])
    questionBank.append(newQuestion)


quiz = QuizBrain(questionBank)

while quiz.still_has_question():
      quiz.next_question()

print(f"You've Completed the quiz")
print(f"Your Final score was : {quiz.score}/{quiz.question_number}")

