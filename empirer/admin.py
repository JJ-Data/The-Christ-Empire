from django.contrib import admin
from .models import Program, Weekly, Live

# Register your models here.

admin.site.register(Program)
admin.site.register(Weekly)
admin.site.register(Live)