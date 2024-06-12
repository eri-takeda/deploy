from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('create_theme', views.create_theme, name='create_theme'),
    path('list_themes', views.list_themes, name='list_themes'),
    path('edit_theme/<int:id>', views.edit_theme, name='edit_theme'),
    path('delete_theme/<int:id>', views.delete_theme, name='delete_theme'),
    path('post_comments/<int:theme_id>', views.post_comments, name='post_comments'),


    path('cat_create/', views.cat_create, name='cat_create'),
    path('cat_list/', views.cat_list, name='cat_list'),
    path('cat_edit/<int:id>/', views.cat_edit, name='cat_edit'),
    path('cat_delete/<int:id>/', views.cat_delete, name='cat_delete'),
    path('cat_comments/<int:cat_id>/', views.cat_comments, name='cat_comments'),
    path('cat_search/', views.cat_search, name='cat_search'),

]