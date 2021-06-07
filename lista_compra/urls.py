from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="lista"),
	path('actualizar_compra/<str:pk>/', views.actualizarCompra, name="actualizar_compra"),
	path('borrar_compra/<str:pk>/', views.borrarCompra, name="borrar_compra"),
]