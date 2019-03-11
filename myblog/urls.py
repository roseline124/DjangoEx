from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.request_index, name="home"),
]