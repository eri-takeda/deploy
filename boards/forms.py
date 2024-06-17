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
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}), max_length=100)

    class Meta:
        model = Comments
        fields = ('comment', )


###################################

from django import forms
from .models import Cats, CatComments

class CreateCatForm(forms.ModelForm):
    BIRTHPLACE_CHOICES = [
        ('', '選択してください'),
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
        ('', '選択してください'),
        ('オス', 'オス'),
        ('メス', 'メス'),
    ]

    AGE_CHOICES = [
        ('', '選択してください'),
        ('0', '0歳'),
        ('1', '1歳'),
        ('2', '2歳'),
        ('3', '3歳'),
        ('4', '4歳'),
        ('5以上', '5歳以上'),
    ]

    COLOR_CHOICES = [
        ('', '選択してください'),
        ('茶', '茶'),
        ('白', '白'),
        ('黒', '黒'),
        ('その他', 'その他'),
    ]

    birthplace = forms.ChoiceField(choices=BIRTHPLACE_CHOICES, label='出生地')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='性別')
    color = forms.ChoiceField(choices=COLOR_CHOICES, label='色')
    age = forms.ChoiceField(choices=AGE_CHOICES, label='年齢')
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
            'spayed': '避妊済',
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['birthplace'].initial = ''  # 出生地の初期値を空に設定
            self.fields['gender'].initial = ''      # 性別の初期値を空に設定
            self.fields['color'].initial = ''       # 色の初期値を空に設定

class EditCatForm(forms.ModelForm):

    GENDER_CHOICES = [
        ('', '選択してください'),        
        ('オス', 'オス'),
        ('メス', 'メス'),
    ]

    COLOR_CHOICES = [
        ('', '選択してください'),
        ('黒', '黒'),
        ('白', '白'),
        ('茶', '茶'),
        ('その他', 'その他'),
    ]

    AGE_CHOICES = [
        ('', '選択してください'),
        ('0', '0歳'),
        ('1', '1歳'),
        ('2', '2歳'),
        ('3', '3歳'),
        ('4', '4歳'),
        ('5', '5歳'),
        ('6', '6歳'),
        ('7', '7歳'),
        ('8', '8歳'),
        ('9', '9歳'),
        ('10', '10歳'),
        ('11', '11歳以上'),
    ]

    PREFECTURE_CHOICES = [
        ('', '選択してください'),
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

    SPAYED_CHOICES = [
        ('', '選択してください'),
        (True, '済'),
        (False, '未'),
    ]


    # image = forms.ImageField(label='写真', required=False)
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES)
    age = forms.ChoiceField(label='年齢', choices=AGE_CHOICES)
    color = forms.ChoiceField(label='毛色', choices=COLOR_CHOICES)
    birthplace = forms.ChoiceField(label='出身地', choices=PREFECTURE_CHOICES)
    spayed = forms.ChoiceField(label='避妊・去勢状況', choices=SPAYED_CHOICES)
    class Meta:
        model = Cats
        fields = ['image', 'gender', 'age', 'color', 'birthplace', 'spayed']

    image = forms.ImageField(label='写真',required=False)

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
from django import forms

class SearchCatForm(forms.Form):
    GENDER_CHOICES = [
        ('', '選択してください'),
        ('オス', 'オス'),
        ('メス', 'メス'),
    ]

    AGE_CHOICES = [
        ('', '選択してください'),
        ('0', '0歳'),
        ('1', '1歳'),
        ('2', '2歳'),
        ('3', '3歳'),
        ('4', '4歳'),
        ('5', '5歳'),
        ('6', '6歳'),
        ('7', '7歳'),
        ('8', '8歳'),
        ('9', '9歳'),
        ('10', '10歳'),
        ('11', '11歳以上'),
    ]

    COLOR_CHOICES = [
        ('', '選択してください'),
        ('白', '白'),
        ('黒', '黒'),
        ('茶', '茶'),
        ('その他', 'その他'),
    ]

    BIRTHPLACE_CHOICES = [
        ('', '選択してください'),
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

    birthplace = forms.ChoiceField(label='出生地', choices=BIRTHPLACE_CHOICES, required=False, initial=None)
    age = forms.ChoiceField(label='年齢', choices=AGE_CHOICES, required=False)
    color = forms.ChoiceField(label='色', choices=COLOR_CHOICES, required=False)
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, required=False)
    spayed = forms.BooleanField(label='避妊・去勢済', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].required = False
        self.fields['color'].required = False
        self.fields['gender'].required = False
        self.fields['spayed'].required = False

