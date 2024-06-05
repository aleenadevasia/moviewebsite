from django.urls import path
from .views import (UserListCreateView, UserRetrieveView, UserUpdateView, UserDestroyView, UserListView,
                    CustomLoginAPIView, AdminLoginAPIView)



urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='user_destroy'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', CustomLoginAPIView.as_view(), name='login'),
    path('admin/',AdminLoginAPIView.as_view(),name='admin_login'),
]
