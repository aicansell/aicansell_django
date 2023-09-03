from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import SignUpSerializer, UserSerializer
from .models import Account, Profile, EmailConfirmationToken
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string

from django.core.mail import send_mail, EmailMessage
from datetime import datetime, timedelta

from rest_framework.views import APIView
from accounts.utils import send_confirmation_email

from django.contrib.sites.shortcuts import get_current_site


# accounts/views.py




@api_view(['POST'])
def register(request):
    data = request.data

    #user = SignUpSerializer(data)
    serializer = SignUpSerializer(data=request.data)

    if serializer.is_valid():
        if not Account.objects.filter(email = data['email']).exists():

            user = Account.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                username = data['email'],
                email = data['email'],
                password = make_password(data['password']),

            )
            return Response({'details':'User created'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'error':'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(serializer.errors)



@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def current_user(request):

    user = UserSerializer(request.user)

    return Response(user.data)

"""def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)

"""

@api_view(['POST']) 
def forgot_password(request):

    data = request.data
    user = get_object_or_404(Account, email = data['email'])

    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes = 30)

    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire_date

    user.profile.save()
    #host = get_current_host(request)
    host = get_current_site(request)

    link = "{host}accounts/reset_password/{token}".format(host=host, token=token)
    body =  "Click on the following link to reset your password {link}".format(link=link)

    send_mail(
        "Password reset link for Aicansell",
        body,
        "info@aicansell.com",
        [data['email']]
    )
    return Response({'details': 'Password reset email sent to {email}'. format(email=data['email'])})



@api_view(['POST']) 
def reset_password(request,token):

    data = request.data
    user = get_object_or_404(Account, profile__reset_password_token = token)

    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response ({"error":"The link has expired"}, status=status.HTTP_400_BAD_REQUEST)

    if data['password'] != data['confirmPassword']:
        return Response ({"error":"The passwords don't match"}, status=status.HTTP_400_BAD_REQUEST)

    user.password =  make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None

    user.profile.save()
    user.save()

    return Response({'details': 'Password has been reset'})


class UserInformationAPIVIew(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        email = user.email
        is_email_confirmed = user.is_email_confirmed
        payload = {'email': email, 'is_email_confirmed': is_email_confirmed, 'id': user.pk}
        return Response(data=payload, status=status.HTTP_200_OK)

class SendEmailConfirmationTokenAPIView(APIView):

    permission_classes = [IsAuthenticated,]

    def post(self, request, format=None):

        user = request.user
        token = EmailConfirmationToken.objects.create(user=user)
        
        send_confirmation_email(email=user.email, token_id=token.pk, user_id=user.pk)
        return Response(data=None, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def confirm_email_view(request):
    token_id = request.GET.get('token_id', None)
    user_id = request.GET.get('user_id', None)
    try:
        token = EmailConfirmationToken.objects.get(pk=token_id)
        user = token.user
        user.is_email_confirmed = True
        user.save()
        data = {'is_email_confirmed': True}
        return Response({'details': 'Email has been confirmed'}, status=status.HTTP_200_OK )
       #return render(request, template_name='users/confirm_email_view.html', context=data)
    except EmailConfirmationToken.DoesNotExist:
        data = {'is_email_confirmed': False}
        return Response({'details': 'Email has not been confirmed'} )
        #return render(request, template_name='users/confirm_email_view.html', context=data)



