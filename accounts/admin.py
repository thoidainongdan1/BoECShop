from django.contrib import admin
from accounts.models import Profile, User

admin.site.register(Profile)
admin.site.register(User)