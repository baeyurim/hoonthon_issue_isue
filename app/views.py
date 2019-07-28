from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Issue, Comment
from django.core.files.storage import FileSystemStorage
from .forms import CommentForm

def index(request):
    issues = Issue.objects.all()
    return render(request, 'index.html', {'issues':issues})

def maker(request):
    return render(request, 'maker.html')

def search(request):          
    title =  request.GET.get('search')
    if title != "":
        status = Issue.objects.filter(title__icontains=title)
    else: 
        status = False
    return render(request,'search.html',{'status':status})


def new(request):
    
    if request.method == 'POST':        
        issue = Issue()

        issue.title = request.POST['title']
        issue.body = request.POST['body']
        issue.key = request.POST['key']
        
           
        images = request.FILES['image']
        im = FileSystemStorage()
        issue.image = im.save(images.name, images)
        
        issue.date = timezone.datetime.now()    
        issue.writer = request.user

        issue.save()
        
        return redirect('/')        

    else:        
        return render(request, 'new.html')


def detail(request, issue_id):
    issue=get_object_or_404(Issue, pk=issue_id)

    return render(request, 'detail.html', {'issue':issue})

def edit(request, issue_id):

    issue = get_object_or_404(Issue, pk=issue_id)

    if request.method == 'GET':
        return render(request, 'edit.html', {'issue':issue})
    
    else:  
        
             
        issue.title = request.POST['title']
        issue.body = request.POST['body']
        issue.key = request.POST['key']
        images = request.FILES['image']
        im = FileSystemStorage()
        issue.image = im.save(images.name, images)
            
        issue.date = timezone.now() 

        issue.save()
    
        return redirect('/' + str(issue_id))


def delete(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    issue.delete()

    return redirect('/')



def signup(request):
    if request.method == 'POST':

        if request.POST['username'] == '' or request.POST['password'] == '':
            return render(request, 'signup.html', {'error':'아이디 비밀번호를 입력하세요'})
        
        if request.POST['password'] != request.POST['con_password']:
            return render(request, 'signup.html', {'error':'비밀번호 불일치'})

        try :
            user = User.objects.get(username = request.POST['username'])
            return render(request, 'signup.html', {'error':'이미 존재하는 이름'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)

            return redirect('/')


    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(request, username = username, password = pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'아이디, 비밀번호 확인'})

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def comment_create(request, issue_id):

        if request.method == 'POST':
                issue = get_object_or_404(Issue, pk=issue_id)
                form = CommentForm(request.POST)
                
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.issue = issue
                        comment.com_writer = request.user

                        comment.save()
                return redirect('/' + str(issue.id))
        else:
                form=CommentForm()
                return render(request, 'detail.html', {'form':form})


def comment_delete(request, issue_id, comment_id):
        issue = get_object_or_404(Issue, pk=issue_id)
        comment = get_object_or_404(Comment, pk=comment_id)

        comment.delete()

        return redirect('/' + str(issue.id))
def filtering(request, filter_id):          
    if filter_id == 0 :
        filter_key = "politics"
        status = Issue.objects.filter(key__icontains=filter_key)
    elif filter_id == 1:
        filter_key = "economy"
        status = Issue.objects.filter(key__icontains=filter_key)
    elif filter_id == 2:
        filter_key = "social"
        status = Issue.objects.filter(key__icontains=filter_key)
    else :
        filter_key = "entertainment"
        status = Issue.objects.filter(key__icontains=filter_key)    

    return render(request,'search.html',{'status':status})
