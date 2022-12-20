from django.urls import path, include

from rest_framework import routers
from .views import RegisterAPI, UserAPI
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register('api/users', UserAPI, 'users')
router.register('api/register', RegisterAPI, 'register')

urlpatterns = [
    path("", include(router.urls)),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

]
