from django.urls import path
from .views import (
    RegistUserView, HomeView, UserLoginView, UserView,UserMypageView,RecruitmentSearchView,UserInfoChangeView,
    GroupMypageView,RecruitmentDetailView,RecruitmentListView
    
)
from .views import CustomLogoutView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    # path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    # path('user_logout/', CustomLogoutView.as_view(), name='user_logout'),
    path('user/', UserView.as_view(), name='user'),
    path('user_mypage/', UserMypageView.as_view(), name='user_mypage'),  # 里親の遷移先
    path('group_mypage/',GroupMypageView.as_view(), name='group_mypage'),  # 保護団体の遷移先
    path('user_logout/', views.custom_logout_view, name='user_logout'),


    path('recruitment_search/', RecruitmentSearchView.as_view(), name='recruitment_search'),
    path('user_info_change/', UserInfoChangeView.as_view(), name='user_info_change'), # type: ignore
    # path('logout/', logout_view, name='logout'),
    # path('recruitment_list/',RecruitmentListView.as_view(), name='recruitment_list'),#募集一覧
    path('recruitment_list/', views.recruitment_list, name='recruitment_list'),
    path('recruitment_detail/',RecruitmentDetailView.as_view(), name='recruitment_detail'),#募集詳細
    path('register_cat/', views.register_cat, name='register_cat'),  # register_catの名前でパスを追加
    
    path('user_edit/', views.user_edit, name='user_edit'),
    # path('change_password/', views.change_password, name='change_password'),

    path('mypage_redirect/', views.MypageRedirectView.as_view(), name='mypage_redirect'),
]
