"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :shopping
# @Date     :2021/8/8 10:21
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import requests,os
from conf.host import *
from libs.login import *
from libs.shop import *

class shopping:
    def __init__(self,inToken):
        self.header =  {"Authorization":inToken}
    def add_shopping_king(self,indata,id):
        url = f"{Host}/shopping/addcategory"
        if indata["restaurant_id"] == "3269":
            indata["restaurant_id"] =id

        res = requests.post(url,data=indata,headers=self.header)
        return res.json()

    def shopping_list(self,indata):
        url = f"{Host}/shopping/v2/myFoods"
        res = requests.get(url,data=indata,headers=self.header)
        return res.json()

if __name__ == '__main__':
    token = Login().login(user,getToken=True)
    shop = Shop(token).shop_list({"page":1,"limit":1})['data']['records'][0]['id']
    food = shopping(token).add_shopping_king({"restaurant_id":""},shop)
    print(food)

# food_init.list_food({"page":1,"limit":1})['data']['records'][0]['restaurant_id']


