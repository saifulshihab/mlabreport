import django_filters
from home.models import lab_report
#from django_filters import CharFilter

class reportFilter(django_filters.FilterSet):
    #srcReport = CharFilter(field_name='p_identity')
    class Meta:
        model = lab_report
        fields = ['p_identity', 'p_name']