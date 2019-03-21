from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""

urlpatterns = [
    path('blog/', views.request_index, name="home"),
    path('blog/book-review/', views.ReviewListView.as_view(), name="book-review"),
    path('blog/book/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),

    # 템플릿 이름을 바꿔줄 수 있다. 
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='myapp/login.html')), 
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]