from django.db import models


class ThemesManager(models.Manager):

    def fetch_all_themes(self):
        return self.order_by('id').all()


class Themes(models.Model):

    title = models.CharField(verbose_name='タイトル', max_length=100)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )

    objects = ThemesManager()

    class Meta:
        db_table = 'themes'


class CommentsManager(models.Manager):
    def fetch_by_theme_id(self, theme_id):
        return self.filter(theme_id=theme_id).order_by('id').all()

class Comments(models.Model):

    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )
    theme = models.ForeignKey(
        'Themes', on_delete=models.CASCADE
    )
    objects = CommentsManager()

    class Meta:
        db_table = 'comments'


#########################################################

from django.contrib.auth.models import User

class CatsManager(models.Manager):
    def fetch_all_cats(self):
        return self.order_by('id').all()

class Cats(models.Model):
    image = models.ImageField()  # 画像
    gender = models.CharField(max_length=10)  # 性別
    age = models.IntegerField()  # 年齢
    color = models.CharField(max_length=50)  # 色
    birthplace = models.CharField(max_length=100)  # 出生地
    spayed = models.CharField(max_length=10)  # 避妊済みかどうか
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )

    objects = CatsManager()

    class Meta:
        db_table = 'cats'

class CatCommentsManager(models.Manager):
    def fetch_by_cat_id(self, cat_id):
        return self.filter(cat_id=cat_id).order_by('id').all()

class CatComments(models.Model):
    comment = models.CharField(max_length=1000)
    text = models.TextField()  # コメントのテキスト

    def __str__(self):
        return self.text

    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )
    cat = models.ForeignKey(
        'Cats', on_delete=models.CASCADE
    )
    objects = CatCommentsManager()

    class Meta:
        db_table = 'cat_comments'
