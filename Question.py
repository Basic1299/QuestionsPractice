class Question:
    def __init__(self, main_part, correct_answer, answers):
        self.main_part = main_part
        self.correct_answer = correct_answer
        self.answers = answers

    def print(self, number):
        print("=======================================================")
        print(f"{number}) {self.main_part}")
        for answer in self.answers:
            print(answer)

        

    
