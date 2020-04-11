import django_filters
from home.models import lab_report

class reportFilter(django_filters.FilterSet):    
    class Meta:
        model = lab_report
        fields = ['p_identity', 'p_name']