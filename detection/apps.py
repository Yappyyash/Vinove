# myapp/apps.py
from django.apps import AppConfig
import threading
from.import activity_tracker

class DetectionConfig(AppConfig):
    name = 'detection'

    def ready(self):
        # Start the activity tracker in a separate thread
        thread = threading.Thread(target=activity_tracker.start_listeners)
        thread.daemon = True  # Daemonize thread to close it on exit
        thread.start()
        
        analysis_thread = threading.Thread(target=activity_tracker.periodic_analysis, args=(300,))
        analysis_thread.daemon = True
        analysis_thread.start()


#Django signals to handle certain errors or perform actions when exceptions occur.

#from django.apps import AppConfig (Already called)

class YourAppConfig(AppConfig):
    name = 'detection'

    def ready(self):
        import detection.signals
