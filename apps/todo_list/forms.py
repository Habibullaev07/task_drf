from ckeditor.widgets import CKEditorWidget
from django import forms
from apps.todo_list.models import Todo


class TodoForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Todo
        fields = '__all__'