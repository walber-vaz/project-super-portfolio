from django.core.validators import MaxLengthValidator, URLValidator
from django.db import models


class Profile(models.Model):
    name = models.CharField(
        max_length=100, validators=[MaxLengthValidator(limit_value=100)]
    )
    github = models.URLField(validators=[URLValidator()])
    linkedin = models.URLField(validators=[URLValidator()])
    bio = models.TextField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(limit_value=500)],
    )

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=50, validators=[MaxLengthValidator(limit_value=50)]
    )
    description = models.TextField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(limit_value=500)],
    )
    github_url = models.URLField(validators=[URLValidator()])
    keyword = models.CharField(
        max_length=50, validators=[MaxLengthValidator(limit_value=50)]
    )
    key_skill = models.CharField(
        max_length=50, validators=[MaxLengthValidator(limit_value=50)]
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='projects'
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(
        max_length=100, validators=[MaxLengthValidator(limit_value=100)]
    )
    url = models.URLField(validators=[URLValidator()])

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        max_length=100, validators=[MaxLengthValidator(limit_value=100)]
    )
    certifying_institution = models.ForeignKey(
        CertifyingInstitution, on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(Profile, related_name='certificates')

    def __str__(self):
        return self.name
