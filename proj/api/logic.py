import redis
import requests

import base64

from django.conf import settings

def get_emotitoken(description, width=None, height=None):
    conn = redis.StrictRedis(host=settings.CONF['REDIS_HOST'], port=settings.CONF['REDIS_PORT'], db=0)
    key = f"{description}.{width}.{height}"
    emotitoken = conn.get(key)
    if emotitoken:
        #check if emotitoken already cached
        emotitoken = base64.b64decode(emotitoken)
        return emotitoken.decode('UTF-8')

    #generate url for request to dnmonster api
    url = settings.CONF['EMOTITOKEN_HOST'] + ":" + settings.CONF['EMOTITOKEN_PORT'] + "/" + f"monster/{description}/"
    if width:
        url += f"?width={width}"
    if height:
        if "width" in url:
            url += f"&height={height}"
        else:
            url += f"?height={height}"
    
    value = requests.get(url).text
    value = base64.b64encode(value)
    conn.set(key, value)
    return value

    