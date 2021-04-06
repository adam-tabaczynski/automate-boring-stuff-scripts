# myMultiplicationQuiz.py - own implementation of multiplication quiz w/ pyinputplus module

# 10 multiplications; 0x0 to 9x9
# If user enters correct answer, program will display 'Correct!' for 1 sec.
# User get three tries before program moves to next question
# Eight seconds after displaying question, the question is marked as incorrect

import random
import pyinputplus as pyip
import time

print("Welcome to multiplication quiz!")
number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    num_one = random.randint(0,9)
    num_two = random.randint(0,9)
    prompt = '#%s: %s times %s: ' % (question_number +1, num_one, num_two)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num_one * num_two)],
                  blockRegexes=[('.*', 'Incorrect!')],
                  timeout=8, limit=3)           

    except pyip.TimeoutException:
         print('Out of time! Next question:')

    except pyip.RetryLimitException:
        print('You hit the limit! Next question:')

    else: # this block runs if there were no exception raised in try block
        print('Correct!')
        number_of_correct_answers += 1
        time.sleep(1) # Pause to let user see the Correct! message.
