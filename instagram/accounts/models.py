from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.shortcuts import resolve_url


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    follower_set = models.ManyToManyField(
        "self", blank=True, symmetrical=False,
    )
    following_set = models.ManyToManyField("self", blank=True)

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number =models.CharField(max_length=13)
    # validators=[RegexValidator(r"^010-?[1-9]\d{3}-?d{4}$")],
    gender = models.CharField(choices=GenderChoices.choices, max_length=1)
    picture = models.ImageField(blank=True, upload_to="accounts/profile/%Y/%m/%d")

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def profile_picture_url(self):
        if self.picture:
            return self.picture.url
        else:
            return resolve_url('pydenticon_image', self.username)