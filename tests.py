import trivia


def test_url():
    assert trivia.response == "https://opentdb.com/api.php?amount=10&category=20&type=boolean"


def player_answer():
    assert trivia.player_answer(bool)


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
