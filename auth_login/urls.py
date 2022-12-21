from django.urls import path, include

from rest_framework import routers
from .views import RegisterAPI, UserAPI, LogoutView
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path('login/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('register/', RegisterAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', LogoutView.as_view()),

]
