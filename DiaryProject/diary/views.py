from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.utils import timezone
# Create your views here.

def home(request):
    diaryList = Diary.objects.all()
    paginator = Paginator(diaryList, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'diary':page})

def detail(request, id):
    diarys = get_object_or_404(Diary, pk=id)
    return render(request, 'detail.html', {'diary':diarys})

def goAdd(request):
    return render(request, 'add.html')

def add(request):
    new_Diary = Diary()
    new_Diary.title = request.POST['title']
    new_Diary.body = request.POST['body']
    new_Diary.weather = request.POST['weather']
    new_Diary.photo = request.FILES['photo']
    new_Diary.time = timezone.now()
    new_Diary.save()
    return redirect('home')

def delete(request, id):
    delete_Diary = Diary.objects.get(id = id)
    delete_Diary.delete()
    return redirect('home')