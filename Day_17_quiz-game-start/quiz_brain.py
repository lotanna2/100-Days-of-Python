class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list ## q_list is a v
        self.score = 0

    def still_has_questions(self): 
        return self.question_number < len(self.question_list) ## checks if the current question number is less than the total number of questions in the question list. If it is, then there are still questions left to ask, and the method returns True. If not, then all questions have been asked, and the method returns False.


    def next_question(self): 
         current_question = self.question_list[self.question_number] ## retrieves the current question object from the question list using the question number as an index 
         self.question_number += 1 ## increments the question number by 1 to move on to the next question in the list
         user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ") ## prompts the user to answer the current question by displaying the question text and asking for a True or False response
        self.check_answer(user_answer, current_question.answer) ## calls the check_answer method to check if the user's answer is correct or not. It passes the user's answer and the correct answer as arguments to the method.

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower(): ## compares the user's answer to the correct answer, ignoring case sensitivity by converting both to lowercase. If they match, then the user's answer is correct.
            self.score += 1 ## increments the score by 1 to reflect the correct answer
            print("You got it right!") ## prints a message to inform the user that they answered correctly
        else: 
            print("That's wrong.") ## prints a message to inform the user that they answered incorrectly
        print(f"The correct answer was: {correct_answer}.") ## prints the correct answer to the question, regardless of whether the user answered correctly or not
        print(f"Your current score is: {self.score}/{self.question_number}\n") ## prints the user's current score and the total number of questions answered so far, along with a newline character for formatting purposes.