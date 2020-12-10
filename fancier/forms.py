from django import forms
from . import models


class NewFancier(forms.ModelForm):
    class Meta:
        model = models.Fancier
        fields = ['name' , 'slug' ,  'country' , 'state' , 'city',
                        'region' , 'street' , 'profilePicture']
