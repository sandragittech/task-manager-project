from django.http import HttpResponse
from django.shortcuts import render

def task_view(request):
    # Dynamic data to be passed to the template
    context = {
        'welcome_message': 'Your Task Management Page',
        'tasks': ['Task 1: Complete report', 'Task 2: Email client', 'Task 3: Plan meeting'],
    }
    return render(request, 'task.html', context)

# Create your views here.
