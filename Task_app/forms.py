from django.forms import ModelForm
from Task_app.models import TaskApp

class TaskAppForm(ModelForm):
    class Meta:
        model = TaskApp
        fields = ['title','status','priority']
