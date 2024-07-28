from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Genre,
    Actor,
    Movie,
    MovieSession,
    CinemaHall,
)
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.prefetch_related("genres", "actors")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.select_related("movie", "cinema_hall")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer
