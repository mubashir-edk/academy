from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import uuid

app_name = 'disha'

urlpatterns = [
    path('office_staff/', views.OfficeStaffAPI.as_view()),
    path('office_staff/<uuid:id>/', views.OfficeStaffAPI.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
