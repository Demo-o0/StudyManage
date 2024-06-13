from django.urls import path
from . import views



urlpatterns = [
    #path('',views.homePage,name='home'),
    path('login/',views.loginPage,name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('register/',views.registerPage,name='register'),
    # path('student/',views.studentPage,name='student'),
    # path('teacher/teacher_exam/',views.teacher_teachingPage,name='teacherExam'),
    # path('teacher/teacher_add_exam/',views.teacher_add_examPage,name='teacherAddExam')

    path('', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]