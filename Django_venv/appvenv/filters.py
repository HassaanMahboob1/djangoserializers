from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Testing


class TestingList(generics.ListAPIView):
    queryset = Testing.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('age')


# Equivalent FilterSet:
class ProductFilter(filters.FilterSet):
    class Meta:
        model = Testing
        fields = ('age')