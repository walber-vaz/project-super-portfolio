from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Certificate, CertifyingInstitution, Profile, Project
from .serializers import (
    CertificateSerializer,
    CertifyingInstitutionSerializer,
    ProfileSerializer,
    ProjectSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            kwargs.get("pk")
            perfil = self.get_object()

            return render(
                request,
                "profile_detail.html",
                {"profile": perfil},
            )
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            kwargs.get("pk")
            instituicao = self.get_object()

            return render(
                request,
                "profile_detail.html",
                {"certifying_institution": instituicao},
            )
        return super().retrieve(request, *args, **kwargs)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            kwargs.get("pk")
            certificado = self.get_object()

            return render(
                request,
                "profile_detail.html",
                {"certificate": certificado},
            )
        return super().retrieve(request, *args, **kwargs)
