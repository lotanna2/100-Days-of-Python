from question_model import Question ## imported the question class
from data import question_data ## imported the question data
from quiz_brain import QuizBrain ## imported the quiz brain class

question_bank = [] ## created an empty list to store the question objects
for question in question_data:
    question_text = question["text"] ## extracted the question text from the dictionary
    question_answer = question["answer"] ## extracted the question answer from the dictionary
    question_new = Question(question_text, question_answer) ## created a new question object
    question_bank.append(question_new) ## added the question object to the question bank
## this code converts the question data from a list of dictionaries into a list of Question objects, 
# which can then be used in a quiz application. 
# Each question object contains the text of the question and the correct answer, making it easy to access and manipulate the questions during the quiz. 

quiz = QuizBrain(question_bank) ## created a new quiz brain object and passed the question bank to it to initialize the quiz and start the quiz. The quiz brain object will keep track of the current question number, score, and the list of questions to be asked.
while quiz.still_has_questions(): ## continues to display questions while there are still questions left in the quiz
    quiz.next_question() ## called the next_question method of the quiz brain object to display the first question to the user and prompt them for an answer. This method will also update the current question number and score based on the user's response.

print("You've completed the quiz.") ## printed a message to inform the user that they have completed the quiz
print(f"Your final score was: {quiz.score}/{quiz.question_list}") ## printed the user's final score and the total number of questions in the quiz. This provides feedback to the user on their performance in the quiz.