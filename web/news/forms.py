
from django import forms
from .models import User,Profile
from django.core.files.images import get_image_dimensions

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date', 'location')

	def clean_avatar(self):
	        avatar = self.cleaned_data['avatar']

	        try:
	            w, h = get_image_dimensions(avatar)

	            #validate dimensions
	            max_width = max_height = 100
	            if w > max_width or h > max_height:
	                raise forms.ValidationError(
	                    u'Please use an image that is '
	                     '%s x %s pixels or smaller.' % (max_width, max_height))

	            #validate content type
	            main, sub = avatar.content_type.split('/')
	            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
	                raise forms.ValidationError(u'Please use a JPEG, '
	                    'GIF or PNG image.')

	            #validate file size
	            if len(avatar) > (20 * 1024):
	                raise forms.ValidationError(
	                    u'Avatar file size may not exceed 20k.')

	        except AttributeError:
	            """
	            Handles case when we are updating the user profile
	            and do not supply a new avatar
	            """
	            pass

	        return avatar