from . import views
from django.urls import path

urlpatterns = [
    path('', views.AcademyHomeView.as_view(),
         name='academy-home'),
]
