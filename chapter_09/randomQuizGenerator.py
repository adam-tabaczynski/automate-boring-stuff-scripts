#! python3
# randoQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
from pathlib import Path

# The quiz data; key - states, values - capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

filesFolder = (Path.cwd() / 'chapter_09//quizFiles')
filesFolder.mkdir() # creates a folder

# Generate 35 quiz files.
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    # Create a folder for files via (Path.cwd() / 'quizFiles').mkdir()
    # create a file GeoQuiz + number
    # create a file AnswersQuiz + number

    
    quizFile = open(f'{str(filesFolder)}\\capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'{str(filesFolder)}\\capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # TODO: Write out the header for the quiz.
    # some eader > GeoQuiz
    # another header > AnswersQuiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz ( Form{quizNum + 1} )')
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.
    # get keys, shuffle them
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    # for each state key, get the value - it's an answer.
    # get 3 random answers?
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

    # TODO: Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}.{answerOptions[i]}\n")
        quizFile.write('\n')
    


    # TODO: Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")

    quizFile.close()
    answerKeyFile.close()
