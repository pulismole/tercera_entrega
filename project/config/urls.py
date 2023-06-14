from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("compra/", include(("compra.urls", "compra"))),
    path("producto/", include(("producto.urls", "producto"))),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)