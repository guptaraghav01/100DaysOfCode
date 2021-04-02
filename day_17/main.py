from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz! 🎆")
print(f"Your final score was {quiz.score}/{quiz.question_number}")


# Output
# Q.1: A slug's blood is green. (True/False):
# true
# You got it right. ✅
# The correct answer was True.
# Your current score is: 1/1

# Q.2: The loudest animal is the African Elephant. (True/False):
# true
# That's wrong. ❌
# The correct answer was False.
# Your current score is: 1/2

# Q.3: Approximately one quarter of human bones are in the feet. (True/False):
# true
# You got it right. ✅
# The correct answer was True.
# Your current score is: 2/3

# Q.4: The total surface area of a human lungs is the size of a football pitch. (True/False):
# true
# You got it right. ✅
# The correct answer was True.
# Your current score is: 3/4

# Q.5: In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat. (True/False):
# false
# That's wrong. ❌
# The correct answer was True.
# Your current score is: 3/5

# Q.6: In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral. (True/False):
# true
# That's wrong. ❌
# The correct answer was False.
# Your current score is: 3/6

# Q.7: It is illegal to pee in the Ocean in Portugal. (True/False):
# true
# You got it right. ✅
# The correct answer was True.
# Your current score is: 4/7

# Q.8: You can lead a cow down stairs but not up stairs. (True/False):
# false
# You got it right. ✅
# The correct answer was False.
# Your current score is: 5/8

# Q.9: Google was originally called 'Backrub'. (True/False):
# false
# That's wrong. ❌
# The correct answer was True.
# Your current score is: 5/9

# Q.10: Buzz Aldrin's mother's maiden name was 'Moon'. (True/False):
# false
# That's wrong. ❌
# The correct answer was True.
# Your current score is: 5/10

# Q.11: No piece of square dry paper can be folded in half more than 7 times. (True/False):
# true
# That's wrong. ❌
# The correct answer was False.
# Your current score is: 5/11

# Q.12: A few ounces of chocolate can to kill a small dog. (True/False):
# false
# That's wrong. ❌
# The correct answer was True.
# Your current score is: 5/12

# You've completed the quiz! 🎆
# Your final score was 5/12
