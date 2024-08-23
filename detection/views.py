from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .activity_tracker import activity_data

def save_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        request.session['user_name'] = name
        return redirect('activity_view')

    return HttpResponse("Invalid request method", status=405)

def activity_view(request):
    # Get the user name from the session
    user_name = request.session.get('user_name', 'Guest')
    
    # Prepare the context with the latest activity data
    context = {
        'status': activity_data.get('status', 'No data'),
        'active_time': activity_data.get('active_time', 'No data'),
        'screenshot_path': activity_data.get('screenshot_path', 'No data'),
        'user_name': user_name
    }
    print(f'{user_name}_{activity_data.get('screenshot_path')}')
    return render(request, 'working.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')



# Rendering error if the network got stuck or breach in between 

# from django.shortcuts import render (Already called)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
