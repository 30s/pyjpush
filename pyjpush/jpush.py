# coding: utf-8

from hashlib import md5

import requests


class JPushClient(object):
    URL = 'http://api.jpush.cn:8800/sendmsg/v2/'

    def __init__(self, app_key, master_secret):
        self.app_key = app_key
        self.master_secret = master_secret

    def get_verification_code(self, sendno, receiver_type, receiver_value):
        m  = md5()
        m.update('%d%d%s%s' % (sendno, receiver_type, receiver_value, self.master_secret))
        return m.hexdigest()

    # def sendmsg(self, sendno, receiver_type, receiver_value, msg_type, msg_content, 
    #             send_description, platform, time_to_live=86400):
    #     vc = self.get_verification_code(sendno, receiver_type, receiver_value)
        

    def notification(self, sendno, receiver_type, receiver_value, 
                     txt, platform, time_to_live=86400):
        vc = self.get_verification_code(sendno, receiver_type, receiver_value)
        payload = {'sendno': sendno,
                   'app_key': self.app_key,
                   'receiver_type': receiver_type,
                   'receiver_value': receiver_value,
                   'verification_code': vc,
                   'txt': txt,
                   'platform': platform,
                   'time_to_live': time_to_live}
        resp = requests.post(JPushClient.URL + 'notification', data=payload)
        return resp.json()


    def custom_message(self, sendno, receiver_type, receiver_value, 
                     txt, platform, time_to_live=86400):
        vc = self.get_verification_code(sendno, receiver_type, receiver_value)
        payload = {'sendno': sendno,
                   'app_key': self.app_key,
                   'receiver_type': receiver_type,
                   'receiver_value': receiver_value,
                   'verification_code': vc,
                   'txt': txt,
                   'platform': platform,
                   'time_to_live': time_to_live}
        resp = requests.post(JPushClient.URL + 'custom_message', data=payload)
        return resp.json()


if __name__=='__main__':
    app_key = ''
    master_secret = ''
    imei = ''
    txt  = 'hello world'
    platform = 'android'
    jpc = JPushClient(app_key, master_secret)
    print jpc.notification(1, 1, imei, txt, platform)
    print jpc.custom_message(1, 1, imei, txt, platform)
