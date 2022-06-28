from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 



urlpatterns= [
    path("", views.inicio),
    path("lista_venta", views.lista_venta),
    path("lista_alquiler", views.lista_alquiler),
    path("lista_turismo", views.lista_turismo),
    path("alta_venta", views.alta_venta),
    path("alta_alquiler", views.alta_alquiler),
    path("alta_turismo", views.alta_turismo),
    path("alta_baja_v", views.alta_baja_form_v),
    path("alta_baja_a", views.alta_baja_form_a),
    path("alta_baja_t", views.alta_baja_form_t),
    path("buscar_barrio_t", views.buscar_barrio_t),
    path("buscar_b_t", views.buscar_b_t),
    path("buscar_barrio_v", views.buscar_barrio_v),
    path("buscar_b_v", views.buscar_b_v),
    path("buscar_barrio_a", views.buscar_barrio_a),
    path("buscar_b_a", views.buscar_b_a),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("elimina_v/<int:id>", views.elimina_v, name="elimina_v"),
    path("elimina_a/<int:id>", views.elimina_a, name="elimina_a"),
    path("elimina_t/<int:id>", views.elimina_t, name="elimina_t"),
    path("editar_venta/<int:id>", views.edit_v, name="editar_venta"),
    path("editar_venta/", views.edit_v, name="editar_venta"),
    path("editarPerfil", views.editarPerfil, name=("editarPerfil")),
    path("readme", views.readme)


]