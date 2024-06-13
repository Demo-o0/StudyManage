from django.contrib.auth import authenticate , login, logout
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Student
from .forms import MyUserCreationForm
from .models import Student
from .forms import StudentForm

# Create your views here.


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')

        try:
            user = User.objects.get(account=account)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, account=account, password=password)
        print(str(user))
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'account OR password does not exit')
    context = {'page': page}
    return render(request, 'login_register.html', context)

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error occurred during registration' + str(form.errors))
    print(str(form))
    return render(request, 'login_register.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('home')

def homePage(request):

    context = {'page': 'home',  }
    return render(request,'home.html',context)

# def studentPage(request):
#     context = {'page': 'student', }
#     return render(request,'teacher/teacher_dashboard.html',context)
#
# def teacher_teachingPage(request):
#     context = {'page': 'teacher', }
#     return render(request,'teacher/teacher_exam.html',context)
#
# def teacher_add_examPage(request):
#     if request.method == 'POST':
#         form = MyStudentCreationForm(request.POST)
#         student = form.save(commit=False)
#         if student.save():
#             messages.success(request, 'successfully added')
#     context = {'page': 'teacher', 'messages':messages}
#     return render(request,'teacher/teacher_add_exam.html',context)



# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
