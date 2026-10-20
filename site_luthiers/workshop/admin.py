from django.contrib import admin

# Register your models here.
from .models import Luthier
from .models import Guitar

admin.site.register(Luthier)
admin.site.register(Guitar)
