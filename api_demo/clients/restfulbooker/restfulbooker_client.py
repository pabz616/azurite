import json
from json import dumps
from uuid import uuid4

from api_demo.clients.base_client import BaseClient
from api_demo.config import BOOKER_URL,BOOKED_RESERVATION, AUTH_URL, USN, PWD
from api_demo.utils.request import APIRequest

class BookerClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BOOKER_URL
        self.reservation_url = BOOKED_RESERVATION
        self.auth_url = AUTH_URL
        self.request = APIRequest()
        
    def createAuthToken(self):
        payload= dumps(
            {
            "username" : USN,
            "password" : PWD
          }
        )
        return self.request.post(self.auth_url, payload, self.headers)
        
    def getAllBookings(self):
        return self.request.get(self.base_url)
    
    def getBookingById(self):
        return self.request.get(self.reservation_url)
    
    def createBooking(self):
        lname = f'User {str(uuid4())}'
        
        payload= dumps(
            {
            "firstname" : "New Booking",
            "lastname" : lname,
            "totalprice" : 1499,
            "depositpaid": True,
            "bookingdates" : {
                "checkin" : "2018-05-01",
                "checkout" : "2019-05-01"
            },
            "additionalneeds" : "Breakfast"
            }
        )
        return self.request.post(self.base_url, payload, self.headers)

    def updateBooking(self):
        payload= dumps(
            {
            "firstname" : "James",
            "lastname" : "Brown",
            "totalprice" : 111,
            "depositpaid": True,
            "bookingdates" : {
                "checkin" : "2023-05-05",
                "checkout" : "2023-05-31"
            },
          }
        )
        return self.request.put(self.reservation_url, payload, self.auth_headers)

    def partialUpdateBooking(self):
        payload= dumps(
            {
            "firstname" : "Charlie",
            "lastname" : "Brown",
            "totalprice" : 404,
            "depositpaid": True,
          }
        )
        return self.request.patch(self.reservation_url, payload, self.auth_headers)    

    def deleteBooking(self):
        return self.request.delete(self.reservation_url, self.auth_headers)
    
    