from django_filters import rest_framework as filters
from .models import User
from django_property_filter import PropertyFilterSet, PropertyNumberFilter


class UserFilter(filters.FilterSet, PropertyFilterSet):
    distance = PropertyNumberFilter(field_name='distance', lookup_expr='lte')

    class Meta:
        model = User
        fields = ('gender', 'first_name', 'last_name', 'distance')
