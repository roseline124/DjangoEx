from django.db import models

# Create your models here.
class File(models.Model) : 

    course = models.CharField(max_length=30)
    csv_file = models.FileField(upload_to="randTeam/csv_file")

    create_date = models.DateTimeField(auto_now_add=True)

    def create(self) :
        self.save()

    def __str__(self) :

        return self.course    

class TimestampModel(models.Model) :

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta : 
        abstract = True 


class Project(TimestampModel) : 

    title = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) : 
        return self.title