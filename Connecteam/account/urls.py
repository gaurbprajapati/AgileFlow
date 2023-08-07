from django.urls import path
from account.views import *
urlpatterns = [
    path('hello/', hello.as_view()),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('userteam/', UserTeamView.as_view(), name="userteam"),
    path('usertask/', UserTaskView.as_view(), name="usertask"),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name='reset-password'),

]
