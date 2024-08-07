import site

from django.contrib import admin
from .models import Test, Bolim, UserTestAttempt

# Register your models here.
admin.site.register(Test)
admin.site.register(Bolim)
admin.site.register(UserTestAttempt)

