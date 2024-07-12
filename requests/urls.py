from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from . import views

app_name = 'requests'

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('status/', views.request_status, name='request_status'),
    path('account/', views.account_info, name='account_info'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='requests:signup'), name='logout'),  # Redirect to signup page after logout
]
