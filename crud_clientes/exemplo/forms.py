from django import forms
from exemplo.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clinte
        fields = '__all__'