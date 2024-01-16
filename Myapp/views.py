from django.shortcuts import get_object_or_404, render, redirect
from .models import User, Question, Answers
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
def index(request):
    if request.method == "POST":
        question = request.POST.get("question")
        pub_date = datetime.now()
        ques = Question(question_text=question, pub_date=pub_date)
        user_instance = User.objects.get(pk=request.user.pk)
        ques.save()
        print(user_instance)
        ques.user.add(user_instance)
        return redirect("index")
    latest_question_list = Question.objects.order_by('-pub_date')
    print(latest_question_list)
    context = {"latest_question_list": latest_question_list,
               "user": request.user}
    return render(request, "index.html", context)


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def loginuser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            print(user)
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return redirect("index")
        else:
            return redirect("index")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        USERNAME = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=USERNAME, email=email, password=password)
        user.save()
        return redirect("/")
    return render(request, "register.html")


@login_required(login_url="login")
def Ask(request):
    return render(request, "ask.html")


@login_required(login_url="login")
def ques_ans(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        answer_text = request.POST.get('answer_text', '')
        ans_date = datetime.now()
        if answer_text != '':
            answer = Answers.objects.create(
                answer_text=answer_text,
                ans_date=ans_date,
            )
            answer.question.add(question)
            answer.user.add(request.user)
            answer.save()
        return redirect("ques_ans", question_id=question_id)
    return render(request, "ques_ans.html", {'question': question, 'answers': question.answers_set.all(), "ans_date": Answers.ans_date})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
