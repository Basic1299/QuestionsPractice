from Question import *

class QuestionsCreator:
    def __init__(self, txt_file):
        self.text = self.txt_file_to_var(txt_file)
        self.questions = []

    def txt_file_to_var(self, txt_file):
        with open(txt_file) as file:
            text = file.readlines()
        return text

    def shuffle(self):
        import random

        random.shuffle(self.questions)

    def create(self):
        question = ""
        correct_answer = ""
        answers = []
        
        for line in self.text:
            line = line[:-1]

            if line[-1] == "?":
                question = line
            elif line[-1] == "*":
                correct_answer = line[0]
                answers.append(line[:-1])
            elif line[0] == "+":
                self.questions.append(Question(question, correct_answer, answers))
                question = ""
                correct_answer = ""
                answers = []
            else:
                answers.append(line)
