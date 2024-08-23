# Using Django signals to handle certain errors or perform actions when exceptions occur.
#apps.py and signals.py are interconnected for error handling

from django.core.signals import got_request_exception
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

@receiver(got_request_exception)
def log_exception(sender, request, **kwargs):
    logger.error(f"Unhandled exception in request: {request}", exc_info=True)
