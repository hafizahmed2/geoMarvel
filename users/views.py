from django.shortcuts import render
from users.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_user(request):
    email = request.GET.get('email')

    try:
        user = User.objects.get(email=email)
        user_data = {'email': user.email, 'username': user.username, 'role': user.role}
        response_dict = {'success': True, 'message': 'User found successfully', 'user': user_data}

        return Response(response_dict, status=200)

    except User.DoesNotExist:
        return Response({'message': 'User does not exist'}, status=404)


@api_view(['GET'])
def get_users(request):
    emails = request.Get.getlist('emails')
    user_id = request.user.id
    role_position = User.objects.get(id=user_id).position

    users = User.objects.filter(email__icontains=emails, role__position__lte=role_position)

    users_data = [{'id': user.id, 'email': user.email, 'position': user.role.position} for user in users]
    response_dict = {'success': True, 'message': 'Users found successfully', 'users': users_data}
    return Response(response_dict, status=200)
