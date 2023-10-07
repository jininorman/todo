from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import task


def add(request):
    task2=task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tasks=task(name=name, priority=priority,date=date)
        tasks.save()
    return render(request,'home.html', {'task':task2})



def update(request,id):
    task1 = task.objects.get(id=id)
    form = TodoForm(instance=task1)
    if request.method=='POST':
        form = TodoForm(request.POST or None,instance=task1)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html',{'form':form,'task':task1})


def delete(request,taskid):
    task1 = task.objects.get(id=taskid)
    if request.method == 'POST':
        task1.delete()
        return redirect('/')
    context = {'task1':task}
    return render(request, 'delete.html',context)



def searchdata(request):
        q=request.GET['query']
        mydictionary ={
           'task' : task.objects.filter(name__contains=q)
        }
        return render(request,'home.html',context=mydictionary)
