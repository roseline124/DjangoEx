from django.shortcuts import render, redirect, get_object_or_404
from .models import File, Question
from .forms import FileForm

# Function Based View (FBV)
def index(request) :
    if request.method == "POST" :
        form = FileForm(request.POST, request.FILES) 

        if form.is_valid() : 
            csv_file = form.save(commit=False)
            csv_file.save()

            return redirect('randTeam/result.html')
    else : 
        form = FileForm()

    return render(request, 'randTeam/index.html', {'form':form})


def result(request) :

    return render(request, 'randTeam/result.html')
