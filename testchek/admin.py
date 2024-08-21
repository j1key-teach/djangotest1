import site

from django.contrib import admin
from .models import Test, Bolim, BolimTest, Category
from django.contrib import admin
from django.core.exceptions import ValidationError

# Register your models here.
admin.site.register(Test)


class BolimTestInline(admin.TabularInline):
    model = BolimTest
    extra = 1


class BolimAdmin(admin.ModelAdmin):
    inlines = [BolimTestInline]

    def save_model(self, request, obj, form, change):
        if not change:
            pass
        else:
            pass
        super().save_model(request, obj, form, change)


admin.site.register(Bolim, BolimAdmin)
admin.site.register(Category)
