from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Flight
from api.serializers import FlightSerializer


@api_view(['GET'])
def all_flights(incoming):
    flights = Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_flight(incoming, pk):
    flight = Flight.objects.get(_id=pk)
    serializer = FlightSerializer(flight, many=False)
    return Response(serializer.data)
