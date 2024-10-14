from django.urls import path
from .views import print_hello, user_data, single_user_data, signup, login

urlpatterns = [
    path('hello/',print_hello),
    path('signup/', signup),
    path('login/', login),
    path('get-all-data/', user_data),
    path('users_data/<str:pk>/', single_user_data),
    # path('users/update/<str:email>/',update_user),  
    # path('users/delete/<str:email>/',delete_user),
]