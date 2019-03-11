from django.db import models
# import pandas as pd #csv_file 정리


# Create your models here.
class File(models.Model) : 

    course = models.CharField(max_length=30)
    csv_file = models.FileField(upload_to="randTeam/csv_file")

    create_date = models.DateTimeField(auto_now_add=True)

    def create(self) :
        self.save()

    def __str__(self) :

        return self.course    

