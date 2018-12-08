from django import forms

from django.core import validators
# for name filed
'''def check_for_z(value):
	if value[0].lower() != 'z' :

		raise forms.ValidationError('name need to start with z')'''



class FormName(forms.Form):
	#name = forms.CharField(validators=[check_for_z])
	name = forms.CharField()

	email = forms.CharField()

	verify_email = forms.EmailField(label='enter your email again')

	text = forms.CharField(widget=forms.Textarea)  

	botcatchet = forms.CharField(required=False,widget=forms.HiddenInput,
										validators=[validators.MaxLengthValidator(0)])


	'''def clean_botcatcher(self):
		bitcatcher = self.cleaned_data['botcatchet']

		if len(botcatchet) > 0:
			raise forms.ValidationError("GOTCHA bOT!")
		return botcatchet'''


	def clean(self):

		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError('make sure same email')