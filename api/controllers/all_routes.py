from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.data import Flights


@api_view(['GET'])
def get_routes(incoming):
    routes = [
        '------  LIVE END POINTS  ---------',
        'POST auth/login/ == Login a user',
        'POST auth/signup/ == Register a user',
        'GET flights/ == Fetch all flights',
        'GET flights/id == Fetch all flights',
        'GET /bookings/ == Fetch all bookings - for only authenticated users',
        'GET /bookings/id == Fetch a booking',
        'POST /create_booking/ === Create a booking',
        'PUT /bookings/<bookingId> == Cancel a booking'
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
