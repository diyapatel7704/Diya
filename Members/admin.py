from django.contrib import admin
from .models import *

# Register your models here.

#admin.site.register(Member)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','verify']


