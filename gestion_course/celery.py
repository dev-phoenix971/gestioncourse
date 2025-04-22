import os
from celery import Celery

# Définition du nom de l'application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tierce_app.settings')

app = Celery('tierce_app')

# Charger la configuration depuis Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Découvrir automatiquement les tâches dans toutes les apps Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
