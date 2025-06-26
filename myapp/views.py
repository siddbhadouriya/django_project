from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.http import HttpResponse
from django.http import JsonResponse


def home(request):
    return HttpResponse("✅ Django JWT API is up and running!")

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user':user_serializer.data

            })
        else:
            return Response({'detail':'Invalid creddentials'},status=400)
        
class DashboardView(APIView):
        permission_classes = (IsAuthenticated,)
        def get(self, request):
             user = request.user
             user_serializer = UserSerializer(user)
             return Response({
                  'message':'Welcome to dashboard',
                  'user': user_serializer.data
                  },200)
        

def get_dummy_cowin_data(request):
    data = {
        "sessions": [
            {
                "center_id": 123456,
                "name": "Community Health Center",
                "state": "Uttar Pradesh",
                "pincode": "226020",
                "fee_type": "Free",
                "fee": 0,
                "available_capacity": "20",
                "available_capacity_dose1": 10,
                "available_capacity_dose2": 10,
                "min_age_limit": 18,
                "vaccine": "COVISHIELD"
            },
            {
                "center_id": 654321,
                "name": "Private Clinic",
                "state": "Uttar Pradesh",
                "pincode": "226020",
                "fee_type": "Paid",
                "fee": 250,
                "available_capacity": "5",
                "available_capacity_dose1": 3,
                "available_capacity_dose2": 2,
                "min_age_limit": 45,
                "vaccine": "COVAXIN"
            }
        ]
    }
    return JsonResponse(data)
