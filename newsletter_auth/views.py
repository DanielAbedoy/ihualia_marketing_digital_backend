from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
##from accounts.serializers import UserSerializer
from newsletter_auth.utils import generate_access_token, generate_refresh_token
import jwt
from django.contrib.auth.hashers import check_password
from backend import settings

from marketing.models import Usuario


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_viw(request):
  response = Response()
  
  usuario = request.data.get("usuario")
  password = request.data.get("password")

  if (usuario is None) or (password is None):
    raise exceptions.AuthenticationFailed('Usuario y contraseña requerida')

  user = ''
  try:
    user = Usuario.objects.get(correo=usuario)
  except:
    raise exceptions.AuthenticationFailed("Usuario no existe")
    

  if (check_password(password, user.password) == False):
  #if (user.password != password):
      raise exceptions.AuthenticationFailed('La contraseña es incorrecta')

  access_token = generate_access_token(user)
  refresh_token = generate_refresh_token(user)

  response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
  response.data = {
    'access_token': access_token,
    'user': user.correo,
  }

  return response


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_protect
def refresh_token_view(request):
  '''
   To obtain a new access_token this view expects 2 important things:
        1. a cookie that contains a valid refresh_token
        2. a header 'X-CSRFTOKEN' with a valid csrf token, client app can get it from cookies "csrftoken"
  '''
  ##User = get_user_model()
  refresh_token = request.COOKIES.get('refreshtoken')
    
  if refresh_token is None:
    raise exceptions.AuthenticationFailed('Authentication credentials were not provided.')
  try:
    payload = jwt.decode(refresh_token, settings.SECRET_REFRESH_KEY, algorithms=['HS256'])
  except jwt.ExpiredSignatureError:
    raise exceptions.AuthenticationFailed('expired refresh token, please login again.')

  user = ''
  try:
    user = Usuario.objects.get(id=payload.get('clave'))  
  except:    
    raise exceptions.AuthenticationFailed('Usuario no encontrado')

  access_token = generate_access_token(user)
    
  return Response({'access_token':access_token, "usuario":user.correo})