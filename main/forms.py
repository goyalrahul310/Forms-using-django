from django import forms
from main import models




class studentform(forms.ModelForm):
	class Meta:
		model = models.Student
		fields = '__all__'


	




