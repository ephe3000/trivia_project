import unittest

import requests
import json


 # get statments
# response = requests.get("https://opentdb.com/api.php?amount=10&category=20&type=boolean")
# questions = response.json()
# my_trivia = questions['results']
#
# count = 0
#
# for question in my_trivia:
#     print("a trivia question:", question['question'])
#
#     player_answer = input('True or False: ')
#     answer = question['correct_answer']
#
#     # set score
#     if player_answer.lower() == answer.lower():
#         count += 1
#     print(count)
#
# print('congratulations, your score was ' + str(count))


def get_questions():
    response = requests.get("https://opentdb.com/api.php?amount=10&category=20&type=boolean")
    questions = response.json()
    return questions['results']


def main():
    my_trivia = get_questions()
    count = 0

    for question in my_trivia:
        print("a trivia question:", question['question'])

        player_answer = input('True or False: ')
        answer = question['correct_answer']

        # set score
        if player_answer.lower() == answer.lower():
            count += 1
        print(count)

    print('congratulations, your score was ' + str(count))

main()


# ---------------------------------------

# START OF QUIZ WITH FUNCTIONS
# plan: pass each input to next function
# make ui
# add multiple choice option

# ----

# # get statments
# def get_questions():
#     response = requests.get("https://opentdb.com/api.php?amount=10&category=20&type=boolean")
#     questions = response.json()
#     return questions['results']
#
#
# def get_question():
#     for question in get_questions():
#         print("a trivia question:", question['question'])
#
# def player_answer():
#     player_answer = input('True or False: ')
#     if player_answer.lower() == correct_answer.lower():
#         count += 1
#         #     update score
#     print(count)
#
# print('congratulations, your score was ' + str(count)) mythology quiz! <3
#
# def main():
#     questions = get_questions()
#     for question in questions:
#         answer = get_player_answer(question) # prints to screen, gets input, checks input, return bool
#         if answer is correct:
#             count + 1