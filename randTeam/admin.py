from django.contrib import admin
from .models import File, Project, FlavorReview, GuessNumbers, Question

# Register your models here.
admin.site.register(File)
admin.site.register(Project)
admin.site.register(FlavorReview)
admin.site.register(GuessNumbers)
admin.site.register(Question)
