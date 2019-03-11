from django import forms
from .models import File

class FileForm(forms.ModelForm) :

    class Meta : 
        model = File
        fields = (
            'course',
            'csv_file'
        )   

        widgets = {
            'title':forms.Textarea(attrs={'rows':1, 'cols':30}),
        }
        
        csv_file = forms.FileField(allow_empty_file=False)

