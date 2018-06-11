# -*- coding:utf-8 -*-
__date__ = '18-6-8 下午1:43'

from django import forms
from .models import Comment
from django.forms import Textarea


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','url','comments']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":"required","size": "25", "tabindex": "1","placeholder":"您的昵称（必填）"}),
            'email': forms.TextInput(attrs={"type": "email", "class": "form-control","required":"required", "size": "25", "tabindex": "2","placeholder":"您的邮箱（必填）"}),
            'url': forms.TextInput(attrs={"type": "url", "class": "form-control","size":"25", "tabindex": "3","placeholder":"您的网址（非必填）"}),
            'comments':Textarea(attrs={"id":"comment-textarea","class": "form-control","required": "required", "cols": "100%","rows": "5", "tabindex": "4","placeholder":"您的评论或留言（必填）"})
        }