from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.data import Flights


#
# def get_routes(incoming):
#     routes = [
#         'POST /auth/signup == Register a user',
#         'POST /auth/login == Login a user',
#         'GET /flights == Fetch all flights',
#         'GET /flights/<flightid> == Fetch a specific flight',
#         'GET /bookings == Fetch all bookings - for only authenticated users',
#         'GET /bookings/<bookingid> == Fetch a booking',
#         'POST /bookings == Create a booking',
#         'PUT /bookings/<bookingId> == Cancel a booking'
#     ]
#     return JsonResponse(routes, safe=False)

@api_view(['GET'])
def get_routes(incoming):
    routes = [

        'POST /auth/signup == Register a user',
        'POST /auth/login == Login a user',
        'GET /flights == Fetch all flights',
        'GET /flights/<flightid> == Fetch a specific flight',
        'GET /bookings == Fetch all bookings - for only authenticated users',
        'GET /bookings/<bookingid> == Fetch a booking',
        'POST /bookings == Create a booking',
        'PUT /bookings/<bookingId> == Cancel a booking',

        '------  LIVE END POINTS  ---------',
        'POST auth/login/ == Login a user',
        'POST auth/signup/ == Register a user',
        'GET flights/ == Fetch all flights',
        'GET flights/1 == Fetch all flights',

        '------  DEMO END POINTS  ---------',
        'GET test_flights/ == Fetch all demo flights',
        'GET /test_flights/1 == Fetch a specific demo flight'

    ]
    return Response(routes)


# === TEST FUNCTIONS ===
@api_view(['GET'])
def test_all_flights(incoming):
    return Response(Flights)


@api_view(['GET'])
def test_get_flight(incoming, pk):
    flight = None

    for i in Flights:
        if i['_id'] == pk:
            flight = i
            break
    return Response(flight)
