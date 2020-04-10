from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='client/index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)