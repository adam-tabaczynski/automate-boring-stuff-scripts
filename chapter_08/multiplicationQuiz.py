import pyinputplus as pyip, random, time

number_of_questions = 10
number_of_correct_answers = 0
for question_number in range(number_of_questions):
    number_one = random.randint(0, 9)
    number_two = random.randint(0, 9)
    prompt = '#%s: %s times %s: ' % (question_number +1, number_one, number_two)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (number_one * number_two)],
                  blockRegexes=[('.*', 'Incorrect!')],
                  timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
        
    except pyip.RetryLimitException:
        print('Out of tries!')

    else: # this block runs if there were no exception raised in try block
        print('Correct!')
        number_of_correct_answers += 1

    time.sleep(1) # Pause to let user see the result.
    print('Score: %s / %s' % (number_of_correct_answers, question_number + 1))
