class User:
    def __init__(self, questions):
        self.questions = questions
        self.correct = 0
        self.wrong = 0

    def practice(self):
        for number, question in enumerate(self.questions.questions):
            question.print(number+1)
            print()

            running = True
            while running:
                running = self.answer(question)

        self.show_final_results()


    def answer(self, question):
        number_of_answers = len(question.answers)
        
        user_input = int(input("your answer: "))
        if user_input > 0 and user_input <= number_of_answers:
            self.counter(user_input, question)
            return False
            
        return True

    def counter(self, user_input, question):
        correct_answer = int(question.correct_answer)
        
        if user_input == correct_answer:
            self.correct += 1
            self.show_result("correct", correct_answer)
        else:
            self.wrong += 1
            self.show_result("wrong", correct_answer)

    def show_result(self, state, correct_answer):
        if state == "correct":
            print("Correct!")
        elif state == "wrong":
            print(f"Wrong! Correct answer is {correct_answer}.")
        print()

    def show_final_results(self):
        print("===============================")
        print(f"Correct answers: {self.correct}")
        print(f"Wrong answers: {self.wrong}")
        print("===============================")
        
