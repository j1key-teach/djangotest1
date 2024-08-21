from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    JUNIOR = 'junior'
    MIDDLE = 'middle'
    SENIOR = 'senior'

    STAGE_CHOICES = [
        (JUNIOR, 'Junior'),
        (MIDDLE, 'Middle'),
        (SENIOR, 'Senior'),
    ]

    stage = models.CharField(max_length=10, choices=STAGE_CHOICES, default=JUNIOR)

    def upgrade_stage(self):
        if self.stage == self.JUNIOR:
            self.stage = self.MIDDLE
        elif self.stage == self.MIDDLE:
            self.stage = self.SENIOR
        self.save()


class Promocode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    valid_until = models.DateTimeField(null=True, blank=True)
    used_by = models.ManyToManyField(User, related_name='used_promocodes', blank=True)

    def is_valid(self):
        if not self.is_active:
            return False
        if self.valid_until and self.valid_until < timezone.now():
            return False
        return True
