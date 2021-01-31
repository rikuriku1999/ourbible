from django import forms
from . import models

SEX_CHOICES = (
    ('男性','男性'),
    ('女性','女性'))

CATEGORY_CHOICES = (
    ('小説','小説'),
    ('漫画','漫画'),
    ('映画','映画'),
    ('アニメ','アニメ'),
    ('実用書','実用書'),
    ('その他','その他')
)

AGE_CHOICES = (
    ('10代','10代'),
    ('20~30代','20~30代'),
    ('40代~50代','40代~50代'),
    ('60歳~','60歳~'),
)

class DetailForm(forms.Form):
    class Meta:
        model = models.Biblemodel
        fields = ('title','content','author','category','url')

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'海辺のカフカ'}
        ),
        max_length=30,
    )
    content = forms.CharField(
        max_length=500,
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder':'例　この本を読んで感動しました。'}
        )
    )
    category = forms.ChoiceField(
        widget = forms.Select,
        choices = CATEGORY_CHOICES
    )
    sex = forms.ChoiceField(
        widget = forms.Select,
        choices = SEX_CHOICES
    )
    age = forms.ChoiceField(
        widget = forms.Select,
        choices = AGE_CHOICES
    )
    url = forms.URLField(
        max_length = 100,
        required = False,
        widget = forms.TextInput(
            attrs={'placeholder':'あれば記入'}
        )
    )
    author = forms.CharField(
        required = True,
        max_length=50,
        widget=forms.TextInput()
    )

class SearchForm(forms.Form):
    search = forms.CharField(
        initial='',
        label='search',
        required = False, # 必須ではない
        widget=forms.TextInput(
        attrs={'placeholder':'キーワードを入力'}
    ))