# from django.shortcuts import render
from django.utils import timezone
from .models import Post, Tag
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
# from django.shortcuts import redirect

def post_list(request):
    # Tagで絞り込む場合
    # URLのクエリパラメータからタグ名を取得
    tag_name = request.GET.get('tag')
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        # 関連する投稿をフィルタリング
        posts = tag.posts.all().order_by('-published_date')
    else:
        # 全ての投稿を取得
        posts = Post.objects.all().order_by('-published_date')
        
    # サイドバーに表示するためのタグ一覧
    all_tags = Tag.objects.all().order_by('name')
            
    # # published_date フィールドを降順(新しい順)にソート
    # posts = Post.objects.all().order_by('-published_date')
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'all_tags': all_tags})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# 画像の編集機能を追加(request.FILES を渡すように修正)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

