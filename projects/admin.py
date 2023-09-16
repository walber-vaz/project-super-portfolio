from django.contrib import admin

from projects.models import (
    Certificate,
    CertifyingInstitution,
    Profile,
    Project,
)

admin.site.register(Certificate)
admin.site.register(CertifyingInstitution)
admin.site.register(Project)
admin.site.register(Profile)
