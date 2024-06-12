from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from .models import Themes, Comments
from django.http import Http404


# Create your views here.
def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        create_theme_form.instance.user = request.user
        create_theme_form.save()
        messages.success(request, '掲示板を作成しました。')
        return redirect('boards:list_themes')
    return render(
        request, 'boards/create_theme.html', context={
            'create_theme_form': create_theme_form,
        }
    )


def list_themes(request):
    themes = Themes.objects.fetch_all_themes() # type: ignore
    return render(
        request, 'boards/list_themes.html', context={
            'themes': themes
        }
    )

def edit_theme(request, id):
    theme = get_object_or_404(Themes, id=id)
    if theme.user.id != request.user.id:
        raise Http404
    edit_theme_form = forms.CreateThemeForm(request.POST or None, instance=theme)
    if edit_theme_form.is_valid():
        edit_theme_form.save()
        messages.success(request, '掲示板を更新しました')
        return redirect('boards:list_themes')
    return render(
        request, 'boards/edit_theme.html', context={
            'edit_theme_form': edit_theme_form,
            'id': id,
        }
    )

def delete_theme(request, id):
    theme = get_object_or_404(Themes, id=id)
    if theme.user.id != request.user.id:
        raise Http404
    delete_theme_form = forms.DeleteThemeForm(request.POST or None)
    if delete_theme_form.is_valid(): # csrf check
        theme.delete()
        messages.success(request, '掲示板を削除しました')
        return redirect('boards:list_themes')
    return render(
        request, 'boards/delete_theme.html', context={
            'delete_theme_form': delete_theme_form,
        }
    )


def post_comments(request, theme_id):
    print(request.user.is_authenticated)
    post_comment_form = forms.PostCommentForm(request.POST or None)
    theme = get_object_or_404(Themes, id=theme_id)
    comments = Comments.objects.fetch_by_theme_id(theme_id) # type: ignore
    if post_comment_form.is_valid():
        post_comment_form.instance.theme = theme
        post_comment_form.instance.user = request.user
        post_comment_form.save()
        return redirect('boards:post_comments', theme_id=theme_id)
    return render(
        request, 'boards/post_comments.html', context={
            'post_comment_form': post_comment_form,
            'theme': theme,
            'comments': comments,
        }
    )

################################################

from .models import Cats, CatComments

# 猫の作成ビュー
def cat_create(request):
    create_cat_form = forms.CreateCatForm(request.POST or None, request.FILES or None)
    if create_cat_form.is_valid():
        create_cat_form.instance.user = request.user
        create_cat_form.save()
        messages.success(request, '猫の情報を作成しました。')
        return redirect('boards:cat_list')
    return render(request, 'boards/cat_create.html', context={'create_cat_form': create_cat_form})

# 猫のリスト表示ビュー
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def cat_list(request):
    cats = Cats.objects.all()  # Catsモデルからデータを取得
    paginator = Paginator(cats, 5)  # ページごとに5件ずつ表示
    page_number = request.GET.get('page')
    try:
        page_cats = paginator.page(page_number)
    except PageNotAnInteger:
        # pageパラメータが整数でない場合、最初のページを表示
        page_cats = paginator.page(1)
    except EmptyPage:
        # pageが範囲外の場合、最後のページを表示
        page_cats = paginator.page(paginator.num_pages)
    return render(request, 'boards/cat_list.html', {'cats': page_cats})


# 猫の編集ビュー
def cat_edit(request, id):
    cat = get_object_or_404(Cats, id=id)
    if cat.user.id != request.user.id:
        raise Http404
    edit_cat_form = forms.EditCatForm(request.POST or None, request.FILES or None, instance=cat)
    if edit_cat_form.is_valid():
        edit_cat_form.save()
        messages.success(request, '猫の情報を更新しました。')
        return redirect('boards:cat_list')
    return render(request, 'boards/cat_edit.html', context={'edit_cat_form': edit_cat_form, 'id': id})

# 猫の削除ビュー
def cat_delete(request, id):
    cat = get_object_or_404(Cats, id=id)
    if cat.user.id != request.user.id:
        raise Http404
    delete_cat_form = forms.DeleteThemeForm(request.POST or None)

    if delete_cat_form.is_valid(): # csrf check
        cat.delete()
        messages.success(request, '猫の情報を削除しました。')
        return redirect('boards:cat_list')
    return render(request, 'boards/cat_delete.html', context={'delete_cat_form': delete_cat_form,})


# 猫へのコメント投稿ビュー
def cat_post_comments(request, cat_id):
    post_comment_form = forms.PostCommentForm(request.POST or None)
    cat = get_object_or_404(Cats, id=cat_id)
    comments = CatComments.objects.filter(cat=cat)
    if post_comment_form.is_valid():
        comment = post_comment_form.save(commit=False)
        comment.user = request.user
        comment.cat = cat
        comment.save()
        return redirect('boards:cat_comments', cat_id=cat_id)
    return render(request, 'boards/cat_post_comments.html', context={'post_comment_form': post_comment_form, 'cat': cat, 'comments': comments})


# 猫のコメント表示ビュー
def cat_comments(request, cat_id):
    cat = get_object_or_404(Cats, id=cat_id)
    comments = CatComments.objects.filter(cat=cat)
    return render(request, 'boards/cat_comments.html', context={'cat': cat, 'comments': comments})



#ねこ検索ビュー
from .forms import SearchCatForm

def cat_search(request):
    form = SearchCatForm()

 # セッションから前回のクエリ情報を取得し、削除する
    if 'cat_search_params' in request.session:
        query_params = request.session['cat_search_params']
        del request.session['cat_search_params']
        form = SearchCatForm(query_params)

    cats = Cats.objects.all()

    # フォームの初期値を設定する
    form.initial = request.GET

    if form.is_valid():
        gender = form.cleaned_data.get('gender')
        age = form.cleaned_data.get('age')
        color = form.cleaned_data.get('color')
        birthplace = form.cleaned_data.get('birthplace')
        spayed = form.cleaned_data.get('spayed')

        if gender:
            cats = cats.filter(gender__icontains=gender)
        if age:
            cats = cats.filter(age__icontains=age)
        if color:
            cats = cats.filter(color__icontains=color)
        if birthplace:
            cats = cats.filter(birthplace__icontains=birthplace)
        if spayed is not None:
            cats = cats.filter(spayed=spayed)

        # セッションに現在のクエリ情報を保存
        request.session['cat_search_params'] = request.GET


    return render(request, 'boards/cat_search.html', {'cat_search_form': form, 'cats': cats})
