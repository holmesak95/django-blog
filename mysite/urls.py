# mysite/urls.py

# To design URLs for an app, create a Python module called urls.py which mapps your views (Python functions) to URL path expressions

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include  # <-- Make sure you have both of these imports.
from rest_framework import routers
from blogging.views import UserViewSet, PostViewSet, CategoryViewSet

# Automatically generates the URL conf for our API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

# Django looks for the variable urlpatterns, which is a sequence of django.urls.path()
urlpatterns = [
    path("admin/", admin.site.urls),
    path("polling/", include("polling.urls")),
    path("", include("blogging.urls")),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
