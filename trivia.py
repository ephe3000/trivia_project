# connect to api
import requests
import json

# get statments
# def det_statements():
response = requests.get("https://opentdb.com/api.php?amount=10&category=17&type=boolean")
questions = response.json()
my_trivia = questions['results']
count = 0

# def play_quiz():
for question in my_trivia:

    print("a trivia question:", question['question'])

    # def player_answer()
    player_answer = input('True or False: ')
    answer = question['correct_answer']

    # set score
    if player_answer.lower() == answer.lower():
        count += 1

        #     update score
        #     update score
    print(count)

print('congratulations, your score was ' + str(count))