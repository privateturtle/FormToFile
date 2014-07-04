from django import forms
from .models import FModel

class formFModel(forms.ModelForm):

    class Meta:
        model = FModel
        fields = ['organame',
                 'orgaaddition',
                 'companyadressname',
                 'companyadressaddition',
                 'companyadressstreet',
                 'companyadresspobox',
                 'companyadresscity',
                 'companyadresscountry',
                 'companyphone',
                 'companyfax',
                 'companyweb',
                 'username',
                 'usersurname',
                 'usermail',
                 'userphone'
                ]