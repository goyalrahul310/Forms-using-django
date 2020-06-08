from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from main import (
	forms,
	models)
# Create your views here.

def students(request):
	students = models.Student.objects.all()
	context = {"students" : students}
	return render(request,'main/student.html',context)	

def addstudents(request):
	studentform = forms.studentform()

	if request.method == "POST":
		studentform = forms.studentform(request.POST)
		if studentform.is_valid():
			student = studentform.save() ;
			return HttpResponseRedirect('/students')

	context = {'studentform' : studentform}
	return render(request,'main/addstudent.html',context)

def detail(request,pk):
	detail = get_object_or_404(models.Student,pk = pk)
	context = {"detail" : detail}
	return render(request,'main/detail.html',context)