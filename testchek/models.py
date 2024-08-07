from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    question = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[('A', 'Option_a'), ('B', 'Option_b'), ('C', 'Option_c'),
                                                             ('D', 'Option_d')])

    def __str__(self):
        return self.question


class Bolim(models.Model):
    title = models.CharField(max_length=255)
    tests = models.ManyToManyField(Test)

    def __str__(self):
        return self.title


class UserTestAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    attempt_count = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    error_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.bolim}"




