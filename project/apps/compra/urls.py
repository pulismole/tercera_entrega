from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="compra/index.html"), name="index"),
    path("compra/create_cliente/", views.ClienteCreate.as_view(), name="cliente_form"),
    path("compra/list/", views.CompraList.as_view(), name="compra_list"),
    path("compra/detail/<int:pk>", views.CompraDetail.as_view(), name="compra_detail"),
    path("compra/create/", views.CompraCreate.as_view(), name="compra_form"),
    path("compra/delete/<int:pk>", views.CompraDelete.as_view(), name="compra_delete"),
    path("compra/update/<int:pk>", views.CompraUpdate.as_view(), name="compra_update"),
]