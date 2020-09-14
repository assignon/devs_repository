from django.contrib import admin
from .models import Works, Tags, Description, ProgLang


admin.site.register(Works)
admin.site.register(Tags)
admin.site.register(Description)
admin.site.register(ProgLang)
