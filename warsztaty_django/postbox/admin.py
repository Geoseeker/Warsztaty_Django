from django.contrib import admin
from .models import Person, Adress, Telephone, Email


admin.site.register([Person, Adress, Telephone, Email])