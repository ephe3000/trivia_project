from trivia import get_questions
from unittest import mock, main, TestCase
import requests


# for use inside test trivia -  e.g. "https://opentdb.com/api.php"
def mock_API_call(*args):
    # it will only return data if it matched the url, which starts with "https://opentdb....
    if args[0].startswith("https://opentdb.com/api.php"):
        # if it matches the url run mock_response
        mock_response = requests.Response()
        # ...run response.header, which is the title for my json questions
        mock_response.headers = {'Content-Type': 'application/json'}
        # run status code and check it's working, so - 200
        mock_response.status_code = 200
        # run to check that the questions are in this format. we are testing for 2
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
