from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .activity_tracker import activity_data





from django.http import JsonResponse
import logging
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


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


#User Input Errors: Submit forms with invalid data and check the response.
#API Request Failures: Change the api_url to an invalid one or simulate a timeout.
#Database Errors: Try saving duplicate data or shut down the database.
#File Upload Errors: Upload files that exceed the size limit or are in an unsupported format.

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        if uploaded_file.size > 5 * 1024 * 1024:  # Limit file size to 5MB
            return JsonResponse({'error': 'File size exceeds the 5MB limit'}, status=400)
        
        if not uploaded_file.name.endswith(('.png', '.jpg', '.jpeg', '.pdf')):
            return JsonResponse({'error': 'Unsupported file format'}, status=400)
        
        try:
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)
            return JsonResponse({'message': 'File uploaded successfully', 'url': file_url}, status=201)
        
        except Exception as e:
            return JsonResponse({'error': f'File upload failed: {str(e)}'}, status=500)

