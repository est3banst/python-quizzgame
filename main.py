from data import question_data
from question_model import Question
from quiz_logic import QuizzBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


new_quiz = QuizzBrain(question_bank)

while new_quiz.still_has_quest():
    new_quiz.next_question()



