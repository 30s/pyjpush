from hashlib import md5

import requests


class JPushClient(object):
    URL = 'http://api.jpush.cn:8800/sendmsg/v2/'

    def __init__(self, app_key, master_secret):
        self.app_key = app_key
        self.master_secret = master_secret

    def sendmsg(self):
        pass

    def notification(self, sendno, receiver_type, receiver_value, 
                     txt, platform, time_to_live=86400):
        m  = md5()
        m.update('%d%d%s%s' % (sendno, receiver_type, receiver_value, self.master_secret))
        payload = {'sendno': sendno,
                   'app_key': self.app_key,
                   'receiver_type': receiver_type,
                   'receiver_value': receiver_value,
                   'verification_code': m.hexdigest(),
                   'txt': txt,
                   'platform': platform,
                   'time_to_live': time_to_live}
        resp = requests.post(JPushClient.URL + 'notification', data=payload)
        return resp.json()


    def custom_message(self):
        pass


if __name__=='__main__':
    app_key = ''
    master_secret = ''
    imei = ''
    txt  = 'hello world'
    platform = 'android'
    jpc = JPushClient(app_key, master_secret)
    print jpc.notification(1, 1, imei, txt, platform)
    
