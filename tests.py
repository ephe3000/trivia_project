from trivia import get_questions
from unittest import mock, main, TestCase
import requests


# inside test url - switcharoo - this will be the 'bad' example given to testtrivia, e.g. "https://opentdb.com/api.php"
def mock_API_call(*args):
    if args[0].startswith("https://opentdb.com/api.php"):
        mock_response = requests.Response()
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.status_code = 200
        type(mock_response).json = mock.Mock(return_value={
            'results': [{'question': 'what is your name?', 'correct_answer': 'ellie'},
                        {'question': 'what is your age?', 'correct_answer': 'OLD'}]
        })
        return mock_response


class TestTrivia(TestCase):
    def test_url(self):
        with mock.patch('requests.get', side_effect=mock_API_call):
            questions = get_questions()
            # assert that there will be 2 questions because we put 2 fake questions in the mock(line 13)
            self.assertEqual(len(questions), 2)


if __name__ == '__main__':
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
