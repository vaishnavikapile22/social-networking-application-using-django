from django.urls import path
from .views import (
    UserSearchView, SendFriendRequestView, FriendRequestActionView,
    ListFriendsView, ListPendingRequestsView, SignupView, index_view, login_view, signup_view
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # API endpoints
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/send/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend-request/action/', FriendRequestActionView.as_view(), name='friend-request-action'),
    path('friends/', ListFriendsView.as_view(), name='list-friends'),
    path('friend-requests/pending/', ListPendingRequestsView.as_view(), name='list-pending-requests'),
    
    # Your other API endpoints go here
    
    # Views for HTML pages
    path('', index_view, name='index'),  # The root URL can point to your index page
    path('login/', login_view, name='login'),  # URL for the login page
    path('signup/', signup_view, name='signup'),  # URL for the signup page
]
