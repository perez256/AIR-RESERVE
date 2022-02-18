from django.urls import path
from api.controllers import all_routes, flights, authenticate

urlpatterns = [
    # Token config
    path('auth/login/', authenticate.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/signup/', authenticate.register_user, name='signup'),
    path('', all_routes.get_routes, name='get_routes'),

    # --- Live EndPoints ---


    path('auth/user/profile/', authenticate.get_user_profile, name='user=profile'),

    path('flights/', flights.all_flights, name='flights'),
    path('flights/<str:pk>', flights.get_flight, name='flight'),

    #    test ---  endpoints
    path('test_flights/', all_routes.test_all_flights, name='test_flights'),
    path('test_flights/<str:pk>', all_routes.test_get_flight, name='test_flight'),

]
