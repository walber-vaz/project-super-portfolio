from collections import OrderedDict

from rest_framework import serializers

from .models import Certificate, CertifyingInstitution, Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, required=False)

    class Meta:
        model = CertifyingInstitution
        fields = '__all__'

    def to_representation(self, instance):
        data = OrderedDict()
        data['id'] = instance.id
        data['name'] = instance.name
        data['url'] = instance.url
        data['certificates'] = CertificateSerializer(
            instance.certificate_set.all(), many=True
        ).data

        return data

    def create(self, validated_data):
        certificates_data = validated_data.pop('certificates')
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=certifying_institution,
                **certificate_data,
            )

        return certifying_institution
