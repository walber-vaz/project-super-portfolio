from rest_framework import serializers

from .models import Certificate, CertifyingInstitution, Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class WithoutCertifyingInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'name', 'timestamp']


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = WithoutCertifyingInstitutionSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ['id', 'name', 'url', 'certificates']

    def create(self, validated_data):
        certificates_data = validated_data.pop('certificates')
        new_certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        for certificate in certificates_data:
            new_certificate = {
                'name': certificate['name'],
                'certifying_institution': new_certifying_institution,
                'profiles': [],
            }
            CertificateSerializer().create(new_certificate)
        return new_certifying_institution
