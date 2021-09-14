from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskModel
		fields = ["task"]
		widgets={"task":forms.Textarea(attrs={"rows":4,"cols":22,"style":"resize:none"})}