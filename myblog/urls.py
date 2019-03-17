from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.request_index, name="home"),
    path('blog/book-review/', views.ReviewListView.as_view(), name="book-review"),
    path('blog/book/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
]