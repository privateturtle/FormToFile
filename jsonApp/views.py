from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from django.template.context import RequestContext
from .models import FModel
from .form import formFModel
import json

# Create your views here.

def FModel(request):
    
    form = formFModel()
    if request.method == 'POST':
        daten = {'Organisation':request.POST['organame'],
                'Organisationzusatz':request.POST['orgaaddition'],
                'Firma':request.POST['companyadressname'],
                'FirmaZusatz':request.POST['companyadressaddition'],
                'Strasse':request.POST['companyadressstreet'],
                'PLZ':request.POST['companyadresspobox'],
                'Ort':request.POST['companyadresscity'],
                'Land':request.POST['companyadresscountry'],
                'Telefon':request.POST['companyphone'],
                'Fax':request.POST['companyfax'],
                'Web':request.POST['companyweb'],
                'UserName':request.POST['username'],
                'Vorname':request.POST['usersurname'],
                'Email':request.POST['usermail'],
                'Telefon':request.POST['userphone']
                }
        print daten
        zeichenkette = json.dumps(daten, indent=4)
        print daten
        new_file = file('json.txt', 'a')
        new_file.write(zeichenkette + "\n")
        new_file.close()
    return render_to_response('index.html', {'form':form}, RequestContext(request))