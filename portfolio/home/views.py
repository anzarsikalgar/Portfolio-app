from django.shortcuts import render
from home.models import Contact
# Create your views here.
def home(request):
    #return HttpResponse("This is home page(/)")
    context={'name':'Anzar','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    #return HttpResponse("This is about page(/about)")
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        print("The data has been written to the db.")

    #return HttpResponse("This is contact page(/contact)")
    return render(request,'contact.html')

def projects(request):
    # return HttpResponse("This is project page(/projects)")
    return render(request,'projects.html')