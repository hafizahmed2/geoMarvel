from users.models import User
from django.http import JsonResponse



def auth_middleware(get_response):
    def middleware(request):
        header = request.headers.get('Authorization')
        token = header.get('auth_token')

        is_valid = parse_token(token)

        if is_valid:
            response = get_response(request)
            return response
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

    return middleware
