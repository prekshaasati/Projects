from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []
for ques in question_data :
    #print(ques)
    a=ques['question']
    b=ques["correct_answer"]
    question_obj = Question(a,b)
    Question_bank.append(question_obj)
    #print(question_obj.text)

# for i in Question_bank :
#     print(Question_bank[0].answer)

quiz_brain = QuizBrain(Question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    #
    #print(quiz_brain.score)
print(f"Your Total Score is {quiz_brain.score}/{quiz_brain.question_number} ")
    





