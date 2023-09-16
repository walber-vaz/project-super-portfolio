from django.urls import include, path
from rest_framework import routers

from .views import ProfileViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'profiles/<int: id>', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'projects/<int: id>', ProjectViewSet)

urlpatterns = [path('', include(router.urls))]
