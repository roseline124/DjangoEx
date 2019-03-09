"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. (urlpatterns 리스트는 url들을 뷰로 라우팅한다.)

Examples:
Function views (함수형 view라면? )
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views (클래스형 view라면? )
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf (다른 URLconf를 포함하려면?)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

URLconf는 뭘까?
- settings.py에 최상위 url이 지정되어 있다 :  ROOT_URLCONF = 'mysite.urls'
- 특정 url과 뷰를 매핑한다.
- Django 서버로 Http 요청이 들어올 때마다, URLConf 매핑 List 를 처음부터 끝까지 순차적으로 훝으며 검색
- 매칭되는 URL Rule 을 찾지못했을 경우, 404 Page Not Found 응답을 발생
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_index, name="home"),
]