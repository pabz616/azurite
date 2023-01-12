import requests
from assertpy.assertpy import assert_that


url = "http://jsonplaceholder.typicode.com/comments"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "f5b4086d-d815-4241-86d0-c8982392de36"
    }

response = requests.get(url, data=payload, headers=headers)


def test_comments_api_response():
    assert response.status_code == 200


def test_comments_api_headers():
    assert ('Content-Type' in response.headers)


def test_comments_api_contract():
    assert ('email' in response.text)


def test_comments_api_content():
    assert ('Jayne_Kuhic@sydney.com'in response.text)






# RESPONSE HAS NO ERRORS

# RESPONSE TIME WAS TO SPEC ('Response time is less than 200ms')