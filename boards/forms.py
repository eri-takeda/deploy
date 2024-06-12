from django import forms
from .models import Themes, Comments


class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')

    class Meta:
        model = Themes
        fields = ('title',)


class DeleteThemeForm(forms.ModelForm):

    class Meta:
        model = Themes
        fields = []

class PostCommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}))

    class Meta:
        model = Comments
        fields = ('comment', )


###################################

from django import forms
from .models import Cats, CatComments

class CreateCatForm(forms.ModelForm):
    BIRTHPLACE_CHOICES = [
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
        ('沖縄県', '沖縄県'),
    ]

    GENDER_CHOICES = [
        ('オス', 'オス'),
        ('メス', 'メス'),
    ]

    COLOR_CHOICES = [
        ('茶', '茶'),
        ('白', '白'),
        ('黒', '黒'),
        ('その他', 'その他'),
    ]

    birthplace = forms.ChoiceField(choices=BIRTHPLACE_CHOICES, label='生まれた場所')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='性別')
    color = forms.ChoiceField(choices=COLOR_CHOICES, label='色')
    image = forms.ImageField(required=False, label='写真')  # 'image' フィールドが必須でないことを明示

    class Meta:
        model = Cats
        fields = ['image', 'gender', 'age', 'color', 'birthplace', 'spayed']
        widgets = {
            'image': forms.ClearableFileInput()  # 'image'フィールドが空でも送信できるようにする
        }

        labels = {
            'image': '画像',
            'age': '年齢',
            'spayed': '避妊済み',
        }


class EditCatForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['image', 'gender', 'age', 'color', 'birthplace', 'spayed']

    image = forms.ImageField(required=False)

class CatCommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}))

    class Meta:
        model = CatComments
        fields = ('comment', )

class DeleteCatForm(forms.ModelForm):

    class Meta:
        model = Cats
        fields = []

from django import forms


#ねこ検索フォーム
class SearchCatForm(forms.Form):
    GENDER_CHOICES = [
        ('オス', 'オス'),
        ('メス', 'メス'),
    ]

    AGE_CHOICES = [
        ('', '選択してください'),
        ('0', '子猫(1歳未満)'),
        ('1', '成猫(1歳以上)'),
    ]

    COLOR_CHOICES = [
        ('', '選択してください'),
        ('白', '白'),
        ('黒', '黒'),
        ('茶', '茶'),
        ('その他', 'その他'),
    ]

    BIRTHPLACE_CHOICES = [
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
        ('沖縄県', '沖縄県'),
    ]

    birthplace = forms.ChoiceField(label='生まれた場所', choices=BIRTHPLACE_CHOICES, required=False)
    age = forms.ChoiceField(label='年齢', choices=AGE_CHOICES, required=False)
    color = forms.ChoiceField(label='色', choices=COLOR_CHOICES, required=False)
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, required=False)
    spayed = forms.BooleanField(label='避妊・去勢済み', required=False)

    class Meta:
        model = Cats
        fields = []

from django import forms
