"""prototipo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from .api import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("api/v1/", include(router.urls)),
    path("django_plotly_dash/", include("django_plotly_dash.urls")),
    path("select2/", include("django_select2.urls")),
    path("", include("core.urls", namespace="core")),
    path("dengue/", include("dengue.urls", namespace="dengue")),
    path("geo/", include("geo.urls", namespace="geo")),
    ]
