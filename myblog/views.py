from django.shortcuts import render
from django.http import HttpResponse
# from . import models

# Create your views here.


#이것도 Q&A에 올리기 
#뷰 -> 템플릿 -> response
def request_index(request) :
    return render(request, "myblog/index.html")

# #템플릿을 거치지 않고 바로 뷰에서 응답 주기 
# def index(request) :
#     return HttpResponse("Hello Babe")
