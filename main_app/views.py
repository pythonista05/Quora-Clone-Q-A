from traceback import format_exc
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def home_page(request):
    questions = Question.objects.all()
    return render(request, 'home_page/home_page.html', {'questions':questions})

def register_user(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'register_page/register_user.html', {'form':form})
    except:
        print("::::::::::::e:::::::::::;", format_exc())
        

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login_page/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home_page')
    else:
        form = QuestionForm()
    return render(request, 'post_question_page/post_question.html', {'form':form})

@login_required
def get_question_detail(request, id):
    question =     question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answers = form.save(commit=False)
            answers.user = request.user
            answers.question = question
            answers.save()
            return redirect('get_question_detail', id=id)
    else:
        form = AnswerForm()
        return render(request, 'question_detail_page/question_detail.html', {'form':form,'question':question,'answers':answers})

@login_required    
def like_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    if answer.user == request.user:
        messages.error(request, "")
    else:
        Like.objects.get_or_create(answer=answer, user=request.user)
    return redirect('get_question_detail', id=answer.question.id)