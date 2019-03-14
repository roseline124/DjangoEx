from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.result, name="result")
    # re_path(r'^result/', views.result, name="result" ),
    # re_path(r'^result/(?P<pk>\d+)/$', views.result, name="result" ),
]
