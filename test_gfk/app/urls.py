from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

ROUTER = DefaultRouter()
ROUTER.register("posts", PostViewSet)
ROUTER.register("comments", CommentViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path("posts/<post_id>/comments", PostComments.as_view()),
    path("", include(ROUTER.urls)),
]