from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    # tagsフィールドを直接指定することで、フォームの表示をカスタマイズ可能
    # 例えば、CheckboxSelectMultipleなどを使用できる
    # tags = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )
    
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'tags')  # 'image','tags' フィールドを追加
        