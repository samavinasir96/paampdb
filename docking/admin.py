from django.contrib import admin
from .models import PDBQuery, AMP, TargetProtein, Dock

admin.site.register(PDBQuery)
admin.site.register(AMP)
admin.site.register(TargetProtein)
admin.site.register(Dock)