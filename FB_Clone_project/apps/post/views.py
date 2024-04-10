from django.shortcuts import render, redirect

from .forms import UserPostForm, UserCommentForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def like(request,post_id):
    user = request.user
    post = UserPost.objects.get(id = post_id)

    liked = Like.objects.get(user=user,post=post).count()
    if not liked :
        like = Like.objects.create(user=user,post=post)
        like.save()
        post.like = post.like + 1
        post.save()

def unlike(request, post_id):
    user = request.user
    post = UserPost.objects.get(id = post_id)
    like = Like.objects.get(user=user,post=post)
    liked = like.count()
    if liked:
        post.like = post.like - 1
        post.save()
        liked.delete()

@login_required
def PostFormView(request):
    if request.method == 'POST':
        fm = UserPostForm(request.POST, request.FILES)
        if fm.is_valid():
            user_post = fm.save(commit=False)
            user_post.user = request.user
            print(request.user)
            
            user_post.save()
            return redirect('Post:dashbord')  # Redirect to dashboard upon successful post creation
    else:
        fm = UserPostForm()
    return render(request, 'post/post.html', {'form': fm})

@login_required
def dashbord(request):
    if request.user.is_authenticated:
        return render(request, 'post/dashbord.html',{'name':request.user})
    return redirect('/')


@login_required
def update_post(request,id):
    if request.method == 'POST':
        new_obj1 = UserPost.objects.get(id = id)
        new_obj1.image = request.POST.get('image')
        
        fm = UserPostForm(request.POST, request.FILES, instance=new_obj1)
        if fm.is_valid():
            fm.save()
        return redirect('Post:dashbord')  # Redirect to dashboard upon successful post creation
    else:
        fm = UserPostForm()
    return render(request, 'post/post.html', {'form': fm})


@login_required
def delete_post(request,id):
    user_post = UserPost.objects.get(id = id)
    user_post.delete()
    user_post = UserPost.objects.filter(user=request.user)
    return render(request, 'post/profile.html',{'user_post':user_post})


@login_required
def all_user_post(request):
    post = UserPost.objects.all().order_by('-created_at')
    # show_cmt
    all_cmt = UserComments.objects.all().order_by('-created_at')
    return render(request,'post/all_user_post.html',{'all_user_post':post,'comment':all_cmt})


@login_required
def view_post(request):
    user_post = UserPost.objects.filter(user=request.user)
    all_cmt = UserComments.objects.all().order_by('-created_at')
    
    return render(request, 'post/profile.html',{'user_post':user_post,'comment':all_cmt})



@login_required
def post_detail(request,post_id):
    user_post = UserPost.objects.get(id = post_id)
    all_cmt = UserComments.objects.all().order_by('-created_at')
    return render(request,'post/post_detail.html',{'post':user_post,'comment':all_cmt})


def comment_on_post(request, post_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if not comment_text:
            return JsonResponse({'success': False, 'message': 'Please add comment...'})
        
        post = UserPost.objects.get(id=post_id)
        new_comment = UserComments.objects.create(user=request.user, post=post, comment=comment_text)
        new_comment.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
