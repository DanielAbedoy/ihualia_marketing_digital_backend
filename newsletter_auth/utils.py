import datetime
import jwt
from django.conf import settings

def generate_access_token(user):
    access_token_payload = {
        'clave':user.id,
        'usuario': user.correo,
        'cliente': user.id_cliente.__str__(),
        'type':"access",
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token

def generate_refresh_token(user):
    refresh_token_payload = {
        'clave':user.id,
        'usuario': user.correo,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(refresh_token_payload, settings.SECRET_REFRESH_KEY, algorithm='HS256').decode('utf-8')
    return refresh_token