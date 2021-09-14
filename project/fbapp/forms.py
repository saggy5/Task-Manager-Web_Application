from django import forms 

class FbForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter your name"}))
	number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"enter your number"}))
	feedback = forms.CharField( widget=forms.Textarea(attrs={"placeholder":"Write Your Feedback here", "rows":6, "cols":22,"style":"resize:none;"}))