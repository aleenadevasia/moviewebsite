from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryRetrieveView,
    CategoryUpdateView,
    CategoryDestroyView,
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='category-retrieve'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDestroyView.as_view(), name='category-delete'),
]
