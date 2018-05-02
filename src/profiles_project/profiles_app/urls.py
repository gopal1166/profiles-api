from .views import TestApiView, TestViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('test-viewset', TestViewSet, base_name='test_viewset')

urlpatterns = [
    url(r'^test/', TestApiView.as_view() ),
    url(r'', include(router.urls) )
]
