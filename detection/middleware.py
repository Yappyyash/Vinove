import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class ExceptionHandlingMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        logger.error(f"Exception occurred: {exception}", exc_info=True)
        return JsonResponse({
            'error': str(exception),
            'message': 'An error occurred. Please try again later.'
        }, status=500)
