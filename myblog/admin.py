from django.contrib import admin
from .models import ReadingList, Book
from randTeam.models import File

# Register your models here.
admin.site.register(ReadingList)
admin.site.register(Book)
admin.site.register(File)

