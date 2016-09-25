from django import forms
from .models import Join

#from django.forms import ModelForm

class EmailForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		#fields = "__all__"
		fields = ['email','ip_adress']