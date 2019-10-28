from django.shortcuts import render
from posts_app.forms import PostsForm
from posts_app.models import postsModel

# Create your views here.

def index(request):
    form = PostsForm()
    print(form)
    data = postsModel.objects.all().order_by('-datetime')
    if request.method =="POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostsForm()
            print("vidation success")
        else:
            print("validation unsuccesssful")
    
    return render(request, 'posts_app/index.html',{'form':form,'data':data})