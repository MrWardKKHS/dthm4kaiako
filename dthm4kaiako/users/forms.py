"""Forms for user application."""

from django.forms import ModelForm
from django.contrib.auth import get_user_model, forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

User = get_user_model()


class SignupForm(ModelForm):
    """Sign up for user registration."""

    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        """Metadata for SignupForm class."""

        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'institution_name',
            'institution_address',
            'membership_category',
        ]

    def signup(self, request, user):
        """Extra logic when a user signs up.

        Required by django-allauth.
        """
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Ensures email = username
        user.institution_name = self.cleaned_data['institution_name']
        user.institution_address = self.cleaned_data['institution_address']
        user.membership_category = self.cleaned_data['membership_category']
        user.is_approved = False
        user.is_paid_up = False
        user.save()


class UserChangeForm(forms.UserChangeForm):
    """Form class for changing user."""

    class Meta(forms.UserChangeForm.Meta):
        """Metadata for UserChangeForm class."""

        model = User
        fields = ('email', 'last_name')


class UserCreationForm(forms.UserCreationForm):
    """Form class for creating user."""

    class Meta(forms.UserCreationForm.Meta):
        """Metadata for UserCreationForm class."""

        model = User
        fields = ('email', 'first_name', 'last_name')

class UserProfileForm(ModelForm):
    """Form for updating user profile information."""

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'institution_name',
            'institution_address',
            'membership_category',
        ]
