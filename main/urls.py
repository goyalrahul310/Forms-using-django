from django.urls import path

from main import views

urlpatterns = [
path('',views.addstudents),
path('students',views.students),
path('detail/<int:pk>',views.detail,name = 'get_detail')

]