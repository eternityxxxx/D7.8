from allauth.account.views import login, signup
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import EditUserProfile


app_name = 'common'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('<int:pk>/edit_profile/', EditUserProfile.as_view(), name='edit-profile'),
]
