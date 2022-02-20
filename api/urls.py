from django.urls import path
from api.controllers import all_routes, flights, authenticate

urlpatterns = [
    # Token config
    path('', all_routes.get_routes, name='get_routes'),
    path('auth/signup/', authenticate.register_user, name='signup'),
    path('auth/login/', authenticate.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/user/profile/', authenticate.get_user_profile, name='user=profile'),

    # --- Live EndPoints ---

    path('flights/', flights.all_flights, name='flights'),
    path('flights/<str:pk>', flights.get_flight, name='flight'),
    path('bookings/', flights.get_bookings, name='bookings'),
    path('bookings/<str:pk>', flights.get_booking_detail, name='get_booking_detail'),
    path('create_booking/', flights.create_booking, name='create_booking'),

    #    test ---  endpoints
    path('test_flights/', all_routes.test_all_flights, name='test_flights'),
    path('test_flights/<str:pk>', all_routes.test_get_flight, name='test_flight'),

]
