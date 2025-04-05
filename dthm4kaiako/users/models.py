"""Models for user application."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from utils.get_upload_filepath import get_entity_upload_path
from django.utils import timezone
from django.urls import reverse


class User(AbstractUser):
    """User of website."""

    username = None  # Remove username field entirely
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=150, verbose_name='last name')

    is_approved = models.BooleanField(default=False)

    institution_name = models.CharField(max_length=255)
    institution_address = models.TextField()

    MEMBERSHIP_CATEGORIES = [
        ('standard', '1 person Membership $50'),
        ('student_teacher', 'Student Teacher (Free)'),
        ('primary', 'Primary (Free)'),
        ('year_7_8', 'Year 7-8 (Free)'),
        ('kura_kaupapa', 'Kura Kaupapa (Free)'),
        ('wider_sector', 'Wider Education Sector'),
    ]

    membership_category = models.CharField(max_length=50, choices=MEMBERSHIP_CATEGORIES)
    is_paid_up = models.BooleanField(default=False)
    membership_expiry = models.DateField(null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'institution_name',
        'institution_address',
        'membership_category',
    ]

    def get_absolute_url(self):
        """Return URL for user's webpage."""
        return reverse('users:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """Name of the user."""
        return f'{self.first_name} {self.last_name}'


class Entity(models.Model):
    """Model for an entity (organisation, company, group, etc)."""

    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(blank=True)
    logo = models.ImageField(
        null=True,
        blank=True,
        upload_to=get_entity_upload_path,
        help_text="Logo will be displayed instead of name if provided."
    )

    def __str__(self):
        """Text representation of a entity."""
        return self.name

    def save(self, *args, **kwargs):
        """Override save method to ensure logo is saved to correct directory.

        The method saves the file once the instance has a primary key,
        as the upload_to function of the file uses this key.

        This method is adapted from the answer at:
        https://stackoverflow.com/a/58853713/10345299
        """
        if self.pk is None:
            saved_image = self.logo
            self.logo = None
            super().save(*args, **kwargs)
            self.logo = saved_image
            kwargs.pop('force_insert', None)
        super().save(*args, **kwargs)

    class Meta:
        """Meta options for class."""

        ordering = ['name', ]
        verbose_name_plural = 'entities'
