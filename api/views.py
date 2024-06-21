from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from .models import FriendRequest
from .serializers import CustomUserSerializer, FriendRequestSerializer, FriendRequestActionSerializer

User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(token),
            'access': str(token.access_token),
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

class UserSearchView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if '@' in query:
            return User.objects.filter(email__iexact=query)
        return User.objects.filter(
            models.Q(first_name__icontains=query) | models.Q(last_name__icontains=query)
        )

class SendFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        to_user_id = request.data.get('to_user_id')
        to_user = User.objects.get(id=to_user_id)
        friend_request, created = FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
        if not created:
            return Response({'message': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Friend request sent'}, status=status.HTTP_201_CREATED)

class FriendRequestActionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = FriendRequestActionSerializer(data=request.data)
        if serializer.is_valid():
            friend_request = FriendRequest.objects.get(id=serializer.validated_data['request_id'])
            if serializer.validated_data['action'] == 'accept':
                friend_request.status = 'accepted'
            elif serializer.validated_data['action'] == 'reject':
                friend_request.status = 'rejected'
            friend_request.save()
            return Response({'message': f'Friend request {friend_request.status}'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListFriendsView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friends = FriendRequest.objects.filter(
            (models.Q(from_user=user) | models.Q(to_user=user)),
            status='accepted'
        )
        friend_ids = [fr.to_user.id if fr.from_user == user else fr.from_user.id for fr in friends]
        return User.objects.filter(id__in=friend_ids)

class ListPendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')

# View for rendering the index page
def index_view(request):
    return render(request, 'index.html')
# View for rendering the login page
def login_view(request):
    return render(request, 'login.html')

# View for rendering the signup page
def signup_view(request):
    return render(request, 'signup.html')

