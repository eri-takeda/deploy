from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import RegistForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.http import require_http_methods
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import RegistForm
from django.http import HttpResponse




class HomeView(TemplateView):
    template_name = 'home.html'


class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm
    
    def form_valid(self, form):
        # フォームのデータを保存
        user = form.save()
        
        user_type = form.cleaned_data['user_type']
        # 里親が選択された場合
        if user_type == 'user':
            # ユーザーを認証してログイン
            user = authenticate(self.request, username=user.email, password=form.cleaned_data['password'])
            if user is not None:
                login(self.request, user)
            # ログイン後のリダイレクト先を指定
            self.success_url = reverse_lazy('accounts:user_mypage')

        # 保護団体が選択された場合
        elif user_type == 'group':
            # ユーザーを認証してログイン
            user = authenticate(self.request, username=user.email, password=form.cleaned_data['password'])
            if user is not None:
                login(self.request, user)
            # ログイン後のリダイレクト先を指定
            self.success_url = reverse_lazy('accounts:group_mypage')
            
            # 登録後に適切なログイン画面にリダイレクト
        return super().form_valid(form)


from .models import Users

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:  # ユーザーがログインしている場合
            if hasattr(user, 'user_type'):
                user_type = user.user_type # type: ignore
                if user_type == 'group':
                    return reverse_lazy('accounts:group_mypage')
        return reverse_lazy('accounts:user_mypage')


    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)

#0604
from .forms import UserEditForm 
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_edit(request):
    user_edit_form = UserEditForm(request.POST or None, request.FILES or None, instance=request.user)
    if user_edit_form.is_valid():
        messages.success(request, '更新完了しました。')
        user_edit_form.save()
    return render(request, 'user_edit.html', context={
        'user_edit_form': user_edit_form,
    })




class UserLogoutView(LogoutView):
    pass


from django.views.decorators.http import require_POST

@method_decorator(require_POST, name='dispatch')
# @method_decorator(require_http_methods(["GET"]), name='dispatch')
class CustomLogoutView(LogoutView):
    pass


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    

class UserMypageView(TemplateView):
    template_name = "user_mypage.html"


#RecuitmentSearchViewの定義
from .forms import RecruitmentSearchForm
from django.shortcuts import render

class RecruitmentSearchView(View):
    template_name = 'recruitment_search.html'

    def get(self, request):
        # GETリクエストに対する処理
        # フォームをインスタンス化してテンプレートに渡す
        form = RecruitmentSearchForm()
        return render(request, self.template_name, {'form': form, 'search_results': None})

    def post(self, request):
        # POSTリクエストに対する処理
        # フォームからデータを取得
        form = RecruitmentSearchForm(request.POST)
        # フォームが有効かチェック
        if form.is_valid():
            # フォームから検索条件を取得
            prefecture = form.cleaned_data['prefecture']
            age = form.cleaned_data['age']
            color = form.cleaned_data['color']
            gender = form.cleaned_data['gender']
            spayed = form.cleaned_data['spayed']
            status = form.cleaned_data['status']
        


#UserInfoChangeViewの定義

from django.views import View
from django.http import HttpResponse

class UserInfoChangeView(View):
    def get(self, request):
        # GETリクエストの処理をここに記述する
        return HttpResponse("UserInfoChangeViewのGETリクエストが処理されました。")

    def post(self, request):
        # POSTリクエストの処理をここに記述する
        return HttpResponse("UserInfoChangeViewのPOSTリクエストが処理されました。")



from django.views.generic import ListView

class MessageBoxView(ListView):

    # あるいは、以下のようにget_queryset()メソッドをオーバーライドすることもできます
    # def get_queryset(self):
    #     return Message.objects.all()

    template_name = 'message_box.html'  # テンプレート名を指定
    context_object_name = 'messages'  # コンテキストオブジェクト名を指定


from django.views.generic.base import TemplateView

class GroupMypageView(TemplateView):
    template_name = "group_mypage.html"

#募集詳細(個人マイページのほう)

from django.views.generic import DetailView
from .models import Recruiting

class RecruitmentDetailView(DetailView):
    model = Recruiting  # ビューで使用するモデルを指定
    template_name = 'recruitment_detail.html'  # レンダリングに使用するテンプレートを指定
    context_object_name = 'recruitment'  # テンプレート内でのコンテキスト変数の名前を指定


# views.py 募集内容変更画面
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat,Recruiting
# from .forms import CatRecruitmentForm # 新しく作成するフォーム
from django.utils.functional import SimpleLazyObject

#クラスベースいったんすべてコメントアウト

# class RecruitmentCreateView(LoginRequiredMixin, CreateView):
#     model = Cat
#     form_class = CatRecruitmentForm  # 新しく作成するフォームを指定
#     template_name = 'recruitment_change.html'
#     success_url = reverse_lazy('accounts:recruitment_list')

#     def form_valid(self, form):
#         # フォームのデータが妥当である場合に呼び出される
#         cat_instance = form.save(commit=False)
#         cat_instance.user = self.request.user  # ユーザーを猫に関連付ける
#         cat_instance.save()
#         recruiting_instance = Recruiting(cat=cat_instance, is_closed=form.cleaned_data['is_closed'])
#         recruiting_instance.save()
#         return super().form_valid(form)

class RecruitmentListView(ListView):
    model = Cat
    template_name = 'recruitment_list.html'

from .models import Cat

def recruitment_list(request):
    cats = Cat.objects.all()
    return render(request, 'recruitment_list.html', {'cats': cats})

# class RecruitmentUpdateView(UpdateView):
#     model = Cat
#     fields = ['image', 'gender', 'age', 'color', 'birthplace', 'spayed']    
#     template_name = 'recruitment_change.html'
#     success_url = reverse_lazy('accounts:recruitment_list')


# class RecruitmentDeleteView(DeleteView):
#     model = Cat
#     # template_name = 'recruitment_confirm_delete.html'
#     template_name = 'recruitment_change.html'

#     success_url = reverse_lazy('accounts:recruitment_list')


# from django.shortcuts import render, redirect
# from .forms import CatRecruitmentForm

# def cat_create(request):
#     if request.method == 'POST':
#         form = CatRecruitmentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:recruitment_list')  # 登録後にリダイレクトするURLを指定してください
#     else:
#         form = CatRecruitmentForm()
#     return render(request, 'recruitment_change.html', {'form': form})



#関数ベース
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Cat


#募集内容変更画面

GENDER_CHOICES = [
    ('male', 'オス'),
    ('female', 'メス'),
]

COLOR_CHOICES = [
    ('black', '黒'),
    ('white', '白'),
    ('brown', '茶'),
    ('other', 'その他'),
]

AGE_CHOICES = [
    (0, '子猫 (1歳未満)'),
    (1, '成猫 (1歳以上)'),
]


PREFECTURE_CHOICES = [
    ('北海道', '北海道'),
    ('青森県', '青森県'),
    ('岩手県', '岩手県'),
    ('宮城県', '宮城県'),
    ('秋田県', '秋田県'),
    ('山形県', '山形県'),
    ('福島県', '福島県'),
    ('茨城県', '茨城県'),
    ('栃木県', '栃木県'),
    ('群馬県', '群馬県'),
    ('埼玉県', '埼玉県'),
    ('千葉県', '千葉県'),
    ('東京都', '東京都'),
    ('神奈川県', '神奈川県'),
    ('新潟県', '新潟県'),
    ('富山県', '富山県'),
    ('石川県', '石川県'),
    ('福井県', '福井県'),
    ('山梨県', '山梨県'),
    ('長野県', '長野県'),
    ('岐阜県', '岐阜県'),
    ('静岡県', '静岡県'),
    ('愛知県', '愛知県'),
    ('三重県', '三重県'),
    ('滋賀県', '滋賀県'),
    ('京都府', '京都府'),
    ('大阪府', '大阪府'),
    ('兵庫県', '兵庫県'),
    ('奈良県', '奈良県'),
    ('和歌山県', '和歌山県'),
    ('鳥取県', '鳥取県'),
    ('島根県', '島根県'),
    ('岡山県', '岡山県'),
    ('広島県', '広島県'),
    ('山口県', '山口県'),
    ('徳島県', '徳島県'),
    ('香川県', '香川県'),
    ('愛媛県', '愛媛県'),
    ('高知県', '高知県'),
    ('福岡県', '福岡県'),
    ('佐賀県', '佐賀県'),
    ('長崎県', '長崎県'),
    ('熊本県', '熊本県'),
    ('大分県', '大分県'),
    ('宮崎県', '宮崎県'),
    ('鹿児島県', '鹿児島県'),
    ('沖縄県', '沖縄県')
]

class CatRecruitmentForm(forms.ModelForm):
    user_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, required=True)
    age = forms.ChoiceField(label='年齢', choices=AGE_CHOICES,required=True)
    color = forms.ChoiceField(label='毛色', choices=COLOR_CHOICES, required=True)
    birthplace = forms.ChoiceField(label='出身地', choices=PREFECTURE_CHOICES, required=True)
    image = forms.ImageField(label='写真', required=True)  
    spayed = forms.BooleanField(label='避妊済み', required=True)
    is_closed = forms.ChoiceField(label='募集状況', choices=[('open', '募集中'), ('closed', '募集終了')], required=True)

    class Meta:
        model = Cat
        fields = ['user_id','gender', 'age', 'color', 'birthplace','image', 'spayed','is_closed']

    def save(self, commit=True):
        cat_instance = super(CatRecruitmentForm, self).save(commit=False)
        if commit:
            cat_instance.user_id = self.cleaned_data['user_id']
            cat_instance.save()
            recruiting_instance = Recruiting(cat=cat_instance, is_closed=self.cleaned_data['is_closed'])
            recruiting_instance.save()
        return cat_instance



#猫の登録画面

from django.shortcuts import render, redirect
# from accounts.models import Users  # カスタムユーザーモデルをインポート
from .forms import CatRegistForm
from .models import Cat
from django.contrib.auth.models import User

@login_required
def register_cat(request):
    if request.method == 'POST':
        form = CatRegistForm(request.POST, request.FILES,user=request.user)
        if form.is_valid():
            cat = form.save()
            # cat = form.save(commit=False)
            # cat.user = request.user  # ログインユーザーの情報を自動的に設定
            # cat.save()
            return redirect('accounts:recruitment_list', cat_id=cat.id)
    else:
        form = CatRegistForm()# ユーザー情報を渡す必要がないので、初期化時にはログインユーザーの情報を渡さない
    return render(request, 'register_cat.html', {'form': form})


# def register_cat(request):
#     if request.method == 'POST':
#         form = CatRegistForm(request.POST,request.FILES)
#         if form.is_valid():
#             cat = form.save(commit=True)
#             if isinstance(request.user, User):  # request.userがUserインスタンスであることを確認
#                 cat.user = request.user  # ログインユーザーを猫の所有者として設定
#                 cat.save()
#                 return redirect('recruitment_list', cat_id=cat.id)
#             else:
#                 # 適切なエラーメッセージを表示するなどの処理を追加
#                 pass
#     else:
#         form = CatRegistForm()
#     return render(request, 'register_cat.html', {'form': form})


def cat_detail(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    return render(request, 'cat_detail.html', {'cat': cat})

def cat_update(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    if request.method == 'POST':
        form = CatRecruitmentForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_detail', cat_id=cat_id)
    else:
        form = CatRecruitmentForm(instance=cat)
    return render(request, 'cat_update.html', {'form': form})

def cat_delete(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    if request.method == 'POST':
        cat.delete()
        return redirect('accounts:recruitment_list')
    return render(request, 'cat_delete.html', {'cat': cat})

