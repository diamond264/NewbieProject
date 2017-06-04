from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from mia.models import Post, Board, Comment, Category
from mia.forms import LoginForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signup_ok')


class UserCreateDone(TemplateView):
    template_name = 'registration/signup_ok.html'


def posts(request, category_id):
    board_list = Board.objects.filter(categoryId=category_id)
    category_list = Category.objects.all()
    board_id = board_list[0].id
    post_list=Post.objects.filter(boardId=board_id)
    context={
        'select_board':1,
        'board_list':board_list,
        'post_list':post_list,
        'select_category':int(category_id),
        'category_list':category_list,
    }
    return render(request,'mia/post.html', context)


def postSelect(request, board_id, category_id):
    board_list = Board.objects.filter(categoryId=category_id)
    category_list = Category.objects.all()
    post_list=Post.objects.filter(boardId=board_id)
    context={
        'select_board':board_id,
        'board_list':board_list,
        'post_list':post_list,
        'select_category':int(category_id),
        'category_list':category_list,
    }
    return render(request,'mia/post.html', context)


def posts_new(request):
    if request.method == "POST":
        board = request.POST["board"]
        title = request.POST["title"]
        photo = request.POST["photo"]
        author = request.user
        content = request.POST["content"]

        boardObj = Board.objects.filter(name=board)

        Post.objects.create(title=title, photo=photo, author=author, content=content, boardId=boardObj[0])

        return HttpResponseRedirect("/posts/%s/%s" % (boardObj[0].categoryId.id,boardObj[0].id))

    else:
        board_list = Board.objects.all()
        context={
            'board_list':board_list,
        }
        return render(request, 'mia/post_new.html', context)


def posts_delete(request,pk):
    post = Post.objects.get(pk=pk)
    board = post.boardId
    post.delete()
    return HttpResponseRedirect("/posts/%s/%s" % (board.categoryId.id,board.id))


def posts_edit(request,pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        board = post.boardId
        post.title = request.POST["title"]
        post.photo = request.POST["photo"]
        post.content = request.POST["content"]
        post.save()
        return HttpResponseRedirect("/posts/%s/%s" % (board.categoryId.id,board.id))

    else:
        pk = pk
        board_list = Board.objects.all()
        context = {
            'pk':pk,
            'board_list':board_list,
        }
        return render(request, 'mia/post_edit.html', context)


def comment_delete(request,pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    board = post.boardId
    category = board.categoryId
    comment.delete()
    return HttpResponseRedirect("/posts/%s/%s/%s" % (category.id,board.id,post.pk))


def comment_new(request,board_id,category_id,pk):
    if request.method == "POST":
        message = request.POST["message"]
        author = request.user

        post = Post.objects.get(pk=pk)

        Comment.objects.create(message=message, author=author, post=post)

        return HttpResponseRedirect(request.path)

    else:
        post = Post.objects.get(pk=pk)
        board_list = Board.objects.filter(categoryId=category_id)
        category_list = Category.objects.all()
        context = {
            'pk': pk,
            'post': post,
            'select_board': board_id,
            'board_list': board_list,
            'select_category': category_id,
            'category_list': category_list,
        }
        return render(request, 'mia/post_detail.html', context)


def home(request):
    category_list = Category.objects.all()
    board_list = Board.objects.all()
    top_list = [650,650,530,510,910,850,680,750,920,770,730,750,850]
    left_list = [620,460,390,630,400,240,230,340,600,630,760,510,810]
    target = []
    for i in range(13) :
        left_list[i] += 70
        target.append((board_list[i],top_list[i],left_list[i]))
    context={
        'category_list':category_list,
        'board_list':board_list,
        'top_list':top_list,
        'left_list':left_list,
        'target':target,
    }
    return render(request,'mia/home.html',context)
