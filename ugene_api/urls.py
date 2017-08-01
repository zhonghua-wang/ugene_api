"""ugene_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from job import views as job_views
from ugene_api import settings

routers = routers.DefaultRouter()
routers.register('users', job_views.UserViewSet, base_name='get_queryset')
routers.register('jobs', job_views.JobViewSet)
routers.register('reports', job_views.ReportViewSet)
routers.register('report-units', job_views.ReportUnitViewSet)
routers.register('mutants', job_views.MutantViewSet)

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^api/', include(routers.urls)),
                  url(r'^auth/', include('djoser.urls.authtoken'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
