from django.shortcuts import render
from . import forms
# Create your views here.

def student_view(request):
	form=forms.StudentForm()
	if request.method=='POST':
		form=forms.StudentForm(request.POST)
		if form.is_valid():
			# form.save(commit=True)
			form.save()#commit shuld not be required 
			print('form data is inserted successfully')
	return render(request,'testapp/register.html',{'form':form})
