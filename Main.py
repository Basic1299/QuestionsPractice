"""
Usage:
txt file to import with questions:
*:correct answer mark, +:question separator. Last line in the file must be "empty".
Below is the example of a correct txt file format to import:

Který svátek slaví Češi i lidé po celém světě 8. března?
1.Den matek
2.Den učitelů
3.Mezinárodní den žen*
4.Mezinárodní den dětí
+
Kterou přílohu tradičně jedí Češi ke smaženému kaprovi v mnoha domácnostech na Štědrý večer?
1.Rýži
2.Těstoviny
3.Bramborový salát*
4.Houskové knedlíky
+

"""


from QuestionsCreator import *
from User import *

file_name = "Questions.txt"

questions = QuestionsCreator(file_name)
questions.create()
questions.shuffle()

user = User(questions)

user.practice()
