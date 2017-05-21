
from django.utils.deprecation import MiddlewareMixin

class WhichDatabaseIsTOUseMIddleware(MiddlewareMixin):
    """middleware to change the view"""
    def process_request(self, request):
        path=request.path
        for string in path.rsplit('/'):
            if '_admin' in string:
                request.session['database']=string.rsplit('_admin')[0]
            else:
                pass
