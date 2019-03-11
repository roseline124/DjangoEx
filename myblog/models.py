from django.db import models

# Create your models here.
class ReadingList(models.Model) :

    BOOK_SCORE = ( #왼쪽이 보여질 것 / 오른쪽이 관리자 페이지에 나올 것.
        ('Awesome', 'Awesome'),
        ('Boring', 'Boring'), 
        ('Choigo', 'Choigo'),
        ('Fuck that', 'Fuck that'),
    )

    #책 제목 
    title = models.CharField(max_length=50)

    #서평 
    review = models.TextField(help_text="가차없이 적어라!!")

    #평점
    score = models.CharField(
        max_length=15,
        choices=BOOK_SCORE,
        default='Awesome',
    )

    #책 정보
    book_info_url = models.URLField() #url이라고 바꿔주기 

    #시작일, 완독일
    start_date = models.DateTimeField(blank=True, null=True) 
    finished_date = models.DateTimeField(
        auto_now_add=True) #편집 불가. 자동으로 오늘 날짜로 맞춘다. #편집 가능하고, 오늘 날짜로 하고 싶으면 datetime.now()를 쓸 것.

    def __str__(self) : 
        return self.title 
    
class Book(models.Model) :

    # title = models.OneToOneField(ReadingList, on_delete=models.CASCADE)
    title = models.ForeignKey('ReadingList', on_delete=models.CASCADE)
    

    writer = models.CharField(max_length=50)

    plot = models.TextField(help_text="줄거리")

    published_year = models.DateTimeField(blank=True)

    def __str__(self) :
        return '%s | %s' % ( self.title, self.writer)
