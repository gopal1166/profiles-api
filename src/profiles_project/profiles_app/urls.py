from . import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^test/', views.TestApiView.as_view() )
]
