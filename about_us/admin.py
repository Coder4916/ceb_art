from django.contrib import admin
from .models import Username, Review


class UsernameAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'username'
        'review',
        'review_date'
    )


admin.site.register(Review)
admin.site.register(Username)
