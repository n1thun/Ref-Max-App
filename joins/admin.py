from django.contrib import admin

# Register your models here.
from .models import Join



class JoinAdmin(admin.ModelAdmin):
	list_display = ['email','__unicode__','name','referrer', 'timestamp', 'updatetime']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)
