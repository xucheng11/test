"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :login
# @Date     :2021/8/1 18:16
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import hashlib,copy,requests
from conf.host import *
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()

class Login:
    def login(self,indata,getToken=False):
        url = f"{Host}/account/sLogin"
        pyaload = copy.copy(indata)
        pyaload["password"]=get_md5(indata["password"])
        res = requests.post(url,data=pyaload)
        print(res)
        if getToken==False:
            return res.json()
        else:
            return res.json()["data"]["token"]



if __name__ == '__main__':
    print(Login().login(user))