from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name="hello_viewset")
router.register('profile', views.UserProfileViewSet) # no need to register base_name for a ModelViewSet
router.register('login', views.LoginViewSet, base_name="login")


urlpatterns = [
  url(r'^hello-view/', views.HelloApiView.as_view()),
  url(r'', include(router.urls)),
]
