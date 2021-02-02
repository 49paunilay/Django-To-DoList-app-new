from django.shortcuts import render
import requests
from django.urls import reverse_lazy
from .models import Todoclass
from .forms import TodoForm
from django.views.generic import DeleteView

# Create your views here.
def todo(request):
    form = TodoForm(request.POST or None)
    if(request.method=="POST"):
        if(form.is_valid()):
            form.save()
    form =TodoForm()
    objects = Todoclass.objects.all()
    count=objects.count()
    context={
        'form':form,
        'work':objects,
        'count':count,
    }
    print(objects)
    return render(request,'index.html',context)

class DeleteWork(DeleteView):
    model = Todoclass
    template_name='confirm.html'
    success_url=reverse_lazy('todo')