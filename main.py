from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bak = []
for i in question_data:
    question_text = i["question"]
    answer_text = i["correct_answer"]
    question = Question(question_text, answer_text)
    question_bak.append(question)

quiz = QuizBrain(question_bak)

while quiz.still_has_question():
    quiz.next_question()

quiz.amount_of_question()
