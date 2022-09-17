from django.contrib import admin

from study.models import CustomerUser


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'email', 'passwd')

admin.site.register(CustomerUser, UserAdmin)