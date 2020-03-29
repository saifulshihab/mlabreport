from django import forms
from home.models import lab_report

class ReportUploadForm(forms.ModelForm):        
    class Meta:
        model = lab_report
        fields = [
            'o_name',
            'p_identity',
            'test_1',
            'test1_desc',            
            'test_2',
            'test2_desc',            
            'test_3',
            'test3_desc',            
            'test_4',
            'test4_desc',            
            'test_5',
            'test5_desc'            
        ]
        labels = {
            'o_name': ('Select Hospital'),
            'p_identity': ('Select Patient'),
        }

