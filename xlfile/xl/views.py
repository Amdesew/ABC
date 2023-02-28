from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from .models import Post
from .models import Grade_One, Grade_Two, Grade_Three, Grade_Four, Grade_Five, Grade_Six, Grade_Seven, Grade_Eight, New_Students

def home(request):
    return render(request, 'home.html')

def student_register(request):
    new_student = New_Students.objects.all()

    if request.method == "POST":
        f_name = request.POST['name']
        st_class = request.POST['wanted_class'] 
        st_phone = request.POST['phone_no']

        new_student = New_Students(
            full_name = f_name,
            phone_number = st_phone,
            wanted_class = st_class
        )

        new_student.save()
        return redirect('/thankyou')
    else:
        print("failed")
 
    return render(request, 'student_register.html')

def student_result(request):
    students = ''
    if 'q' in request.GET:
        q = request.GET['q']
        students = Grade_One.objects.filter(ተ_ቁ=q) or Grade_Two.objects.filter(ተ_ቁ=q) or  Grade_Three.objects.filter(ተ_ቁ=q) or Grade_Four.objects.filter(ተ_ቁ=q) or Grade_Five.objects.filter(ተ_ቁ=q) or Grade_Six.objects.filter(ተ_ቁ=q) or Grade_Seven.objects.filter(ተ_ቁ=q) or Grade_Eight.objects.filter(ተ_ቁ=q)
                    
    else:
        print("Failed")
    return render(request, 'student_result.html', {'students': students})

def email(request): 
    send_mail(
        'Subject here',
        'Here is the message.',
        'amdesewseifu7@example.com',
        ['frankamde7 7@example.com'],
        fail_silently=False,
    )
    return render(request, 'notification.html')

def about_us(request):
    return render(request, 'about_us.html')

def back_door(request):
    return render(request, 'back_door.html')

def thankyou_page(request):
    return render(request, 'thankyou.html')


@login_required(login_url="/login")
def admin_home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/home.html', {"posts": posts})


@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/news")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/news')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
