from django.urls import path,include
from .views import UploadEmployeeData
urlpatterns = [
    path('upload/',UploadEmployeeData.as_view(),name='Upload-Excel'),    
]