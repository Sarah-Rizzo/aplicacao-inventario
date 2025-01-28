from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventario_app import views

router = DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

