
import datetime
import jwt
import pytz
import traceback
import os
from dotenv import load_dotenv

# Logger

from app.utils.Logger import Logger
load_dotenv()

class Security():

     #poner la key en el .env mas adelante
    secret = os.getenv("SECRET")
    tz = pytz.timezone("America/Lima")

    @classmethod
    def generate_token(cls, email):
        try:
            payload = {
                'iat': datetime.datetime.now(tz=cls.tz),
                'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=500),
                'email': email,
                'roles': ['Administrator', 'Editor']
            }
            return jwt.encode(payload, cls.secret, algorithm="HS256")
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def verify_token(cls, headers):
        try:
            if 'Authorization' in headers.keys():
                authorization = headers['Authorization']
                encoded_token = authorization.split(" ")[1]

                if ((len(encoded_token) > 0) and (encoded_token.count('.') == 2)):
                    try:
                        payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                        
                        #acordarse que con esta mecanica de los roles se puede aplicar
                        #para los roles del aeroclub tengan acceso a ciertos endpoint
                        """
                         roles = list(payload['roles'])

                        if 'Administrator' in roles:
                            return True
                        return False
                        """
                        
                        return True
                    except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                        return False

            return False
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
