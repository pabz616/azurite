from assertpy import assert_that
import requests

def confirm_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
def confirm_created_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.created)

def confirm_booking_data(resp_body):
    
    assert_that(resp_body['bookingid']).is_not_none().is_greater_than(0).is_type_of(int)
    assert_that(resp_body['booking']).is_not_empty()
    # assert_that(response.text).extracting('firstname').is_not_empty()

