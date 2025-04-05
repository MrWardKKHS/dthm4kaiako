"""Signals for the user application."""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from allauth.account.signals import user_logged_in
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

user_model = get_user_model()


@receiver(post_save, sender=user_model)
def create_user_profile(sender, instance, created, **kwargs):
    """Add automated value for username."""
    if created:
        instance.username = 'user{}'.format(instance.id)
        instance.save()


@receiver(user_logged_in)
def check_approval(sender, request, user, **kwargs):
    if not user.is_approved:
        logout(request)
        messages.error(request, "Your account is pending approval.")
