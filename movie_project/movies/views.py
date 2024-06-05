from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Movie, Review
from .serializers import MovieCreateSerializer, MovieDetailSerializer, ReviewSerializer

class MovieCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated
    parser_classes = [MultiPartParser, FormParser]  # Ensure parsers are set for file uploads

    def post(self, request, *args, **kwargs):
        serializer = MovieCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                movie = serializer.save()
                return Response(MovieCreateSerializer(movie).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(f"Error occurred: {e}")  # Log the error
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class MovieRetrieveView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class MovieUpdateView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class MovieDestroyView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
