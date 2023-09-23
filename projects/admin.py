from django.contrib import admin

from projects.models import (
    Certificate,
    CertifyingInstitution,
    Profile,
    Project,
)


class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.register(Certificate)
admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
admin.site.register(Project)
admin.site.register(Profile)
