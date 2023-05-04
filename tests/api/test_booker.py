import pytest
import json

from api_demo.utils import request
from api_demo.clients.restfulbooker.restfulbooker_client import BookerClient
from api_demo.assertions.booker_assertions import *

client = BookerClient()

def test_create_auth_token():
    response = client.createAuthToken()
    resp_body = json.loads(response.text)
    confirm_response_status(response, 200)
    assert_that(resp_body['token']).is_not_empty()

def test_get_all_bookings():
    response = client.getAllBookings()
    confirm_response_status(response, 200)
 
def test_get_booking_by_id():
    response = client.getBookingById()
    confirm_response_status(response, 200)
    
def test_create_booking():
    response = client.createBooking()
    new_booking = json.loads(response.text)
    confirm_response_status(response, 200)
    confirm_booking_data(new_booking)
    
def test_update_booking():
    response = client.updateBooking()
    confirm_response_status(response, 200)

def test_partial_update_booking():
    response = client.partialUpdateBooking()
    confirm_response_status(response, 200)

def test_delete_booking():
    response = client.deleteBooking()
    confirm_created_status(response, 201)






