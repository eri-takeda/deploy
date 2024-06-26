from django import forms
from .models import Users,Cat, Recruiting,User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

PREFECTURES = [
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

AGE = [
    ('', '選択してください'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),
    ('51', '51'),
    ('52', '52'),
    ('53', '53'),
    ('54', '54'),
    ('55', '55'),
    ('56', '56'),
    ('57', '57'),
    ('58', '58'),
    ('59', '59'),
    ('60', '60'),
    ('61', '61'),
    ('62', '62'),
    ('63', '63'),
    ('64', '64'),
    ('65', '65'),
    ('66', '66'),
    ('67', '67'),
    ('68', '68'),
    ('69', '69'),
    ('70', '70'),
    ('71', '71'),
    ('72', '72'),
    ('73', '73'),
    ('74', '74'),
    ('75', '75'),
    ('76', '76'),
    ('77', '77'),
    ('78', '78'),
    ('79', '79'),
    ('80', '80'),
    ('81', '81'),
    ('82', '82'),
    ('83', '83'),
    ('84', '84'),
    ('85', '85'),
    ('86', '86'),
    ('87', '87'),
    ('88', '88'),
    ('89', '89'),
    ('90', '90'),
    ('91', '91'),
    ('92', '92'),
    ('93', '93'),
    ('94', '94'),
    ('95', '95'),
    ('96', '96'),
    ('97', '97'),
    ('98', '98'),
    ('99', '99'),
    ('100', '100'),
]

USER_TYPE = [ 
    ('', '選択してください'),
    ('user', '里親'), 
    ('group', '保護団体')
]

from django.core.exceptions import ValidationError
class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.ChoiceField(label='年齢', choices=AGE)
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    prefecture = forms.ChoiceField(label='都道府県', choices=PREFECTURES)
    address = forms.CharField(label='住所', max_length=100, required=True)  # required=Trueで必須フィールドに設定
    user_type = forms.ChoiceField(label='ユーザタイプ', choices=USER_TYPE)  # 追加

    class Meta:
        model = Users
        fields = ['username', 'age', 'email', 'password', 'prefecture', 'address', 'user_type']  # 追加    
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            try:
                validate_password(password, self.instance)
            except ValidationError as e:
                self.add_error('password', e)  # パスワードフィールドにエラーメッセージを追加
                raise ValidationError('パスワードが無効です') from e
        else:
            raise ValidationError('パスワードが必要です')

        return password
    

    def clean_address(self):
        address = self.cleaned_data['address']
        if not address:
            raise forms.ValidationError('住所は必須です')  # 空欄の場合にバリデーションエラーを発生させる
        return address
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user




class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)


PREFECTURES = [
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

AGE = [
    ('', '選択してください'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),
    ('51', '51'),
    ('52', '52'),
    ('53', '53'),
    ('54', '54'),
    ('55', '55'),
    ('56', '56'),
    ('57', '57'),
    ('58', '58'),
    ('59', '59'),
    ('60', '60'),
    ('61', '61'),
    ('62', '62'),
    ('63', '63'),
    ('64', '64'),
    ('65', '65'),
    ('66', '66'),
    ('67', '67'),
    ('68', '68'),
    ('69', '69'),
    ('70', '70'),
    ('71', '71'),
    ('72', '72'),
    ('73', '73'),
    ('74', '74'),
    ('75', '75'),
    ('76', '76'),
    ('77', '77'),
    ('78', '78'),
    ('79', '79'),
    ('80', '80'),
    ('81', '81'),
    ('82', '82'),
    ('83', '83'),
    ('84', '84'),
    ('85', '85'),
    ('86', '86'),
    ('87', '87'),
    ('88', '88'),
    ('89', '89'),
    ('90', '90'),
    ('91', '91'),
    ('92', '92'),
    ('93', '93'),
    ('94', '94'),
    ('95', '95'),
    ('96', '96'),
    ('97', '97'),
    ('98', '98'),
    ('99', '99'),
    ('100', '100'),
]

USER_TYPE = [ 
    ('', '選択してください'),
    ('user', '里親'), 
    ('group', '保護団体')
]

class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.ChoiceField(label='年齢', choices=AGE)
    email = forms.EmailField(label='メールアドレス')
    prefecture = forms.ChoiceField(label='都道府県', choices=PREFECTURES)
    address = forms.CharField(label='住所')  
    user_type = forms.ChoiceField(label='ユーザタイプ', choices=USER_TYPE) 
    class Meta:
        model = Users
        fields = ('username', 'age', 'email','prefecture', 'address', 'user_type')

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # 初期値の設定
            if self.instance:
                self.fields['age'].initial = self.instance.age  # ユーザーの年齢を初期値として設定

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
                user.save()
        return user

class RecruitmentSearchForm(forms.Form):
    prefecture = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    color = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    spayed = forms.BooleanField(required=False)
    status = forms.CharField(max_length=100)


#猫の登録

GENDER_CHOICES = [
    ('オス', 'オス'),
    ('オス', 'メス'),
]

COLOR_CHOICES = [
    ('黒', '黒'),
    ('白', '白'),
    ('茶', '茶'),
    ('その他', 'その他'),
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
SPAYED_CHOICES = [
        (True, '済'),
        (False, '未'),
    ]

class CatRegistForm(forms.ModelForm):
    # user = forms.CharField(widget=forms.HiddenInput())
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, required=True)
    age = forms.ChoiceField(label='年齢', choices=AGE_CHOICES,required=True)
    color = forms.ChoiceField(label='毛色', choices=COLOR_CHOICES, required=True)
    birthplace = forms.ChoiceField(label='出身地', choices=PREFECTURE_CHOICES, required=True)
    image = forms.ImageField(label='写真', required=True)  
    spayed = forms.ChoiceField(label='去勢状況', choices=SPAYED_CHOICES, widget=forms.RadioSelect(), required=True)
    is_closed = forms.ChoiceField(label='募集状況', choices=[('True', '募集中'), ('False', '募集終了')], required=True)

    user = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # ログインユーザーを取得
        initial = kwargs.get('initial', {})
        initial['user'] = user.id if user else None
        kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def clean_user(self):
        return None  # user フィールドはバリデーションに関係がないため、何もしない

    class Meta:
        model = Cat
        fields = ['user','gender', 'age', 'color', 'birthplace','image', 'spayed','is_closed']

    def save(self, commit=True):
        cat_instance = super(CatRegistForm, self).save(commit=False)
        if commit:
            cat_instance.user = self.initial.get('user')  # フォームの初期値からユーザーを取得
            cat_instance.save()
            recruiting_instance = Recruiting(cat=cat_instance, is_closed=self.cleaned_data['is_closed'])
            recruiting_instance.save()
        return cat_instance

