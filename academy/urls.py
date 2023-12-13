from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AcademyHomeView.as_view(),
         name='academy-home'),
]
