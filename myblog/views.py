from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from myblog.models import ReadingList, Book
from django.views.generic import ListView, DetailView

# Create your views here.
def request_index(request):
    return render(request, "myblog/index.html")

#리스트 뷰 만들기 
class ReviewListView(ListView): 
    """
	ListView 디폴트 지정 속성 : 컨텍스트를 쓸 때, model만 쓸 때 
	1) 컨텍스트 변수 : object_list
	2) 템플릿 파일 : readinglist_list.html (모델명 소문자_list.html)
	"""
    model = ReadingList
    template_name = 'myblog/review_list.html'
    paginate_by = 1

#디테일 뷰 만들기
class BookDetailView(DetailView):
    model = Book # 해당 모델 - URLConf 의 PK 변수를 활용하여 해당 모델의 특정 record를 컨텍스트 변수(object)에 담는다.
    template_name = 'myblog/book_detail.html' # 디폴트 템플릿명: <app_label>/<model_name>_detail.html
    context_object_name = 'book' # 디폴트 컨텍스트 변수명 :  object