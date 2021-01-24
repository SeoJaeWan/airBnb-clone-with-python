from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(models.User)
class CustomUSerAdmin(UserAdmin):

    """ Custom User Model """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "langauge",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )
