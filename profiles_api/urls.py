from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet

# Registering the viewset
router = DefaultRouter()

"""  base_name should only be provided when the  queryset object is not available in the viewset
or we want to override the name of queryset """

router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')

# registering UserProfile ViewSet (No need to provide base_name bcz queryset is used in  UserProfile )
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('apiview/', HelloApiView.as_view()),
    path('', include(router.urls))  # It will automatically render all the path from router so no need to provide path
]
