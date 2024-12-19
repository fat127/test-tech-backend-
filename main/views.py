from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Villa
from .serializers import VillaSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json

@csrf_exempt
def login_view(request):
    """
    Handles user login using Django's default User model and authenticate function.
    """
    if request.method != 'POST':
        return JsonResponse({"error": "Invalid HTTP method. Use POST."}, status=405)

    try:
        # Parse JSON data from the request body
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON payload."}, status=400)

    # Validate username and password
    if not username or not password:
        return JsonResponse({"error": "Username and password are required."}, status=400)

    print(f"Attempting login for username: {username}")  # Debugging output

    # Use Django's built-in authenticate method
    user = authenticate(request, username=username, password=password)

    if user is not None:
        if not user.is_active:
            return JsonResponse({"error": "User account is inactive."}, status=403)

        login(request, user)
        return JsonResponse({
            "message": "Login successful",
            "username": user.username,
            "is_superuser": user.is_superuser
        }, status=200)
    else:
        print("Authentication failed.")  # Debugging output
        return JsonResponse({"error": "Invalid username or password."}, status=401)

@api_view(['POST'])
def logout_view(request):
    """
    Logs out the currently authenticated user.
    """
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"message": "Logout successful."}, status=200)
    return JsonResponse({"error": "User is not authenticated."}, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])  
def get_user(request):
    """
    Retrieves the currently authenticated user's details.
    """
    if request.user.is_authenticated:
        return JsonResponse({
            "username": request.user.username,
            "is_superuser": request.user.is_superuser
        }, status=200)
    return JsonResponse({"error": "User is not authenticated."}, status=401)

@api_view(['GET'])
def villa_list(request):
    """
    Returns the list of all villas without requiring authentication.
    """
    print("hello")
    villas = Villa.objects.all()
    serializer = VillaSerializer(villas, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def villa_detail(request, id):
    """
    Returns details of a specific villa.
    """
    try:
        villa = Villa.objects.get(pk=id)
        serializer = VillaSerializer(villa)
        return Response(serializer.data, status=200)
    except Villa.DoesNotExist:
        return Response({"error": "Villa not found."}, status=404)
