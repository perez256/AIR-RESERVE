from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Flight, Booking
from api.serializers import FlightSerializer, BookingSerializer


# /flights/
@api_view(['GET'])
def all_flights(incoming):
    flights = Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# /flights/id
@api_view(['GET', 'PUT'])
def get_flight(incoming, pk):
    flight = Flight.objects.get(_id=pk)
    if incoming.method == 'GET':
        try:
            serializer = FlightSerializer(flight, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Flight.DoesNotExist:
            return Response({'message': 'This Flight Ticket does not Exist', }, status=status.HTTP_400_BAD_REQUEST)
    elif incoming.method == 'PUT':
        try:
            flight_data = JSONParser().parse(incoming)
            flight_serializer = FlightSerializer(flight, data=flight_data)
            if flight_serializer.is_valid():
                flight_serializer.save()
                return Response(flight_serializer.data, status=status.HTTP_201_CREATED)
            return Response(flight_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as p:
            print(str(p))
            return Response({'message': 'Failed to update Flight'}, status=status.HTTP_304_NOT_MODIFIED)


# /bookings/
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_bookings(incoming):
    ticket = Booking.objects.all()
    serializer = BookingSerializer(ticket, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# /create_booking/
@api_view(['POST'])
def create_booking(incoming):
    if incoming.method == 'POST':
        try:
            # booking_data = JSONParser().parse(incoming)
            data = incoming.data
            booking_serializer = BookingSerializer(data=data)
            if booking_serializer.is_valid():
                booking_serializer.save()
                return Response(booking_serializer.data, status=status.HTTP_201_CREATED)
            return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as p:
            print(str(p))
            return Response({'message': 'Failed to create a booking'}, status=status.HTTP_304_NOT_MODIFIED)
    else:
        return Response({'message': 'Only Posting data data is allowed'}, status=status.HTTP_400_BAD_REQUEST)


# /bookings/id
@api_view(['GET', 'PUT', 'DELETE'])
def get_booking_detail(incoming, pk):
    ticket = Booking.objects.get(_id=pk)
    if incoming.method == 'GET':
        try:
            serializer = BookingSerializer(ticket, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Flight.DoesNotExist:
            return Response({'message': 'This Ticket does not Exist'}, status=status.HTTP_400_BAD_REQUEST)
    elif incoming.method == 'PUT':
        try:
            booking_data = JSONParser().parse(incoming)
            booking_serializer = BookingSerializer(ticket, data=booking_data)
            if booking_serializer.is_valid():
                booking_serializer.save()
                return Response(booking_serializer.data, status=status.HTTP_201_CREATED)
            return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as p:
            print(str(p))
            return Response({'message': 'Failed to update a booking'}, status=status.HTTP_304_NOT_MODIFIED)

    elif incoming.method == 'DELETE':
        try:
            ticket.delete()
            return Response({'message': 'Ticket was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except Flight.DoesNotExist:
            return Response({'message': 'Delete Failed'}, status=status.HTTP_304_NOT_MODIFIED)
