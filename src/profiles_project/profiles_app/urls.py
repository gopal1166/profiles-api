from .views import TestApiView, TestViewSet, UserProfileViewSet, LoginViewSet, ProfileFeedViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('test-viewset', TestViewSet, base_name='test_viewset')
router.register('profile', UserProfileViewSet) #no need  base_name for ModelViewsets
router.register('login', LoginViewSet, base_name='login_viewset')
router.register('feed', ProfileFeedViewSet)

urlpatterns = [
    url(r'^test/', TestApiView.as_view() ),
    url(r'', include(router.urls) )
]
