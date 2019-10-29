from django.shortcuts import render
from posts_app.forms import PostsForm, ReplyForm
from posts_app.models import postsModel, replyModel

# Create your views here.

def index(request):
    form = PostsForm()
    data = postsModel.objects.all().order_by('-datetime')
    replyData = replyModel.objects.all()
    print(replyData.values('replyTo'))
    if request.method =="POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostsForm()
            print("vidation success")
        else:
            print("validation unsuccesssful")
    
    return render(request, 'posts_app/index.html',{'form':form,'data':data,'replyData':replyData})

def replyView(request):
    form = ReplyForm()
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReplyForm()
            print("reply form validation success")
        else:
            print("reply form validatuon unsucessful")
    return render(request, 'posts_app/reply.html', {'form':form})