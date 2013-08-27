# -*- coding: utf-8 -*-

from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'text': CKEditorWidget()}