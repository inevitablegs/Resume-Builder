from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.resume_form, name='resume_form'),
    path('preview/<int:resume_id>/', views.preview_resume, name='preview_resume'),
    path('download/<int:resume_id>/', views.download_pdf, name='download_pdf'),
]
