class Question: ## this function defines a class called Question, which represents a single question in the quiz. The class has two attributes: text and answer, which store the text of the question and the correct answer, respectively. The __init__ method is called when a new instance of the class is created, and it initializes the text and answer attributes with the values passed as arguments.

    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer

new_q = Question("A slug's blood is green.", "True")
print(new_q.answer)