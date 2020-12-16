from django import forms

from .models import Claim



class NewClaim(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['empno','eiqama','piqama','name']
        