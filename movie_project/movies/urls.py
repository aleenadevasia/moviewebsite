from django.urls import path
from .views import MovieListView, MovieCreateView, MovieRetrieveView, MovieUpdateView, MovieDestroyView, ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('create/', MovieCreateView.as_view(), name='movie-create'),
    path('detail/<int:pk>/', MovieRetrieveView.as_view(), name='movie-retrieve'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('delete/<int:pk>/', MovieDestroyView.as_view(), name='movie-delete'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]




