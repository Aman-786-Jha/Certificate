# certificates/admin.py
from django.contrib import admin
from .models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)

admin.site.register(Certificate, CertificateAdmin)

