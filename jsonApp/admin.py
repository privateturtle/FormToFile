from django.contrib import admin
from jsonApp.models import FModel
# Register your models here.
class FModelAdmin(admin.ModelAdmin):
	pass

admin.site.register(FModel, FModelAdmin)