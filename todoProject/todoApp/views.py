from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm,UserRegistrationForm
from django.contrib import messages
# Create your views here.

def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if is_finished == 'on':
                    finished = True
                else:
                    finished = False
            except:            
                finished = False
        todos = Todo(
            user = request.user,
            title = request.POST['title'],
            is_finished = finished
        )     
        todos.save()
        messages.success(request,f"Task Added from {request.user.username} ")   
    else:            
        form = TodoForm()
    
    todos = Todo.objects.filter(user= request.user)
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False 
    completed_tasks = []
    pending_tasks = []
    for todo in todos:
        if todo.is_finished==True:
            completed_tasks.append(todo)
        else:
            pending_tasks.append(todo)    
    context = {
        'todos':todos,
        'form':form,
        'todo_done':todos_done,
        'completed_tasks':completed_tasks,
        'pending_tasks':pending_tasks
    }
    return render(request,'todoApp/home.html',context)


def update_todo(request,pk=None):
    todo = Todo.objects.get(id=pk) 
    if todo.is_finished == True:
        todo.is_finished = False 
    else:
        todo.is_finished = True
    
    todo.save()
    return redirect('todo')



def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}!!")
            return redirect("login")
    else:        
        form = UserRegistrationForm()
    context = {
        'form':form
        }
    return render(request,'todoApp/register.html',context)

