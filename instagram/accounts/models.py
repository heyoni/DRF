from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number =models.CharField(validators=[RegexValidator(r"^010-?[1-9]\d{3}-?d{4}$")],max_length=13)
    gender = models.CharField(choices=GenderChoices.choices, max_length=1)
    picture = models.ImageField(blank=True, upload_to="accounts/profile/%Y/%m/%d")