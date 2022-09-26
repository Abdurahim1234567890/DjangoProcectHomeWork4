from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from brands.views import *
from models.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', brands),
    path('brands/<int:id>', one_brand),
    path('brands/<int:brand_id>/models/<int:model_id>', one_brand_model_series),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)