import unittest

from trivia import get_questions
from unittest.mock import patch

class
def test_url():
    with patch('trivia.requests.get') as mocked_get:
        mocked_get.assert_called_with("https://opentdb.com/api.php?amount=10&category=20&type=boolean")


if __main__ -- '__main__':
    main()


# def player_answer():
#     assert trivia.player_answer(bool)


# FUNCTION QUIZ TESTS
# check for url

# # check url ok
# def get_url():
#     # arrange/connect to api
#     url = "https://opentdb.com/api.php?amount=10&category=17&type=boolean"
#     # act/get json questions
#     response = requests.get(url)
#     body = response.json()
#     #  assert
#     assert response.status_code == 200
#     assert 'Python' in body['AbstractText']
