#TODO :asking the question
#TODO:CHECKING IF THE ANS IS CORECT 
#TODO : checking if we are at the end of the quiz

from data import question_data

class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def check_ans(self,current_ans,correct_ans):
        
        if current_ans.lower() == correct_ans.lower() :
            print("it's Correct !")
            self.score+=1
        else :
            print("it's Wrong")
        print(f"Your score is {self.score}/{self.question_number}\n")
        print(f"the correct answer was {correct_ans}")


    def next_question(self):
        current_question  = self.question_list[self.question_number]
        self.question_number+=1
        current_ans = input( f"Q.{self.question_number}: {current_question.text} (True/False) ? :").lower()
        self.check_ans(current_ans,current_question.answer)
        return current_ans

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #     return True
        # else :
        #     return False
        

        # return score
    
  
        

        



        



        
