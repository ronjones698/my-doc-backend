from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

router.register('user', views.UsersView,basename='user')
router.register('hospital',views.HospitalView,basename='hospital')
router.register('company',views.CompanyView,basename='company')


urlpatterns = [
    path('',include(router.urls)),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('token/obtain/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain')

]