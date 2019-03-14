from django.contrib import admin
from .models import ReadingList, Book

# Register your models here.
admin.site.register(ReadingList)
admin.site.register(Book)

