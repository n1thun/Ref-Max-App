from django import forms
from .models import Join

# class EmailForm(forms.Form):  #General form method
# 	name = forms.CharField(required=True)
# 	email = forms.EmailField(required=False)


class JoinForm(forms.ModelForm):  #Model form method
	class Meta:
		model = Join
		fields = ['name','email']
