"""api_doc URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from docs.views import EmployeeRegisterView, PositionViewSet, EmployeeRetrieveUpdateDestroyAPIView,\
    PositionRetrieveUpdateDestroyAPIView


schema_view = get_schema_view(
   openapi.Info(
      title="Только я и бог знаем как работает этот код...",
      default_version='v0.01',
      description="...отныне только бог.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="spasite@gmail.com"),
      license=openapi.License(name="Лицензии нет, как и понимания всего того, как это работает "),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),

    path('api/employee/', EmployeeRegisterView.as_view()),
    path('api/employee/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view()),

    path('api/position/', PositionViewSet.as_view()),
    path('api/position/<int:pk>/', PositionRetrieveUpdateDestroyAPIView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
    path('json_doc/', schema_view.without_ui(cache_timeout=0), name='json_doc'),

]
