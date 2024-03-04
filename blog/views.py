from django.shortcuts import render

from django.http import HttpResponse
posts = [{ 'name': 'Yeshwanth','title': 'Blog Post 1' , 'content': 'College Joined', 'date': '26 JAN 2050'},  {'name': 'kishore','title': 'Blog Post 2', 'content': 'going to join college','date': '31 JAN 2100'  }]


def about(request):
    return HttpResponse('<h1> This is django</h1>')
def end(request):
    return HttpResponse('<h1> End Page</h1>')

def home(request):
    context  ={                  #creating a dictionary with a values of previous list
        "posts":posts
    }
    return render(request ,"home.html",context)     #3rd argument will be passes to the template we can access fro  there





