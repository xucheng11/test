"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :shop
# @Date     :2021/8/7 13:49
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import requests
from conf.host import *
from libs.login import Login
class Shop:
    def __init__(self,inToken):
        self.header = {"Authorization":inToken}
    #店铺列出
    def shop_list(self,indata):
        url = f"{Host}/shopping/myShop"
        pyaload = indata
        res=requests.get(url,data=pyaload,headers=self.header)
        return res.json()

    #上传图片
    def shop_file(self,fileName,fileDir):
        url = f"{Host}/file"
        user_file = {"file":(fileName,open(fileDir,"rb"),'image/png')}
        res = requests.post(url,files=user_file,headers=self.header)
        return res.json()["data"]["realFileName"]

    #编辑商铺信息
    def shop_update(self,indata,shopid,imageInfo):
        url = f"{Host}/shopping/updatemyshop"
        indata["id"] =shopid
        indata["image"] =f"{Host}/file/getImgStream?fileName={imageInfo}"
        indata["image_path"] =imageInfo
        res = requests.post(url,data=indata,headers=self.header)
        return res.json()



if __name__ == '__main__':
    token =Login().login(user,getToken=True)
    SHOP = Shop(token)
    shopid = SHOP.shop_list({"limit":1,"page":1})['data']['records'][0]['id']

    # imageInfo = SHOP.shop_file("aaa.png","../data/aaa.png")
    # inf={
    #         "name": "星巴克新建店",
    #         "address": "上海市静安区秣陵路303号",
    #         "id": "3269",
    #         "Phone": "13176876632",
    #         "rating": "6.0",
    #         "recent_order_num":100,
    #         "category": "快餐便当/简餐",
    #         "description": "满30减5，满60减8",
    #         "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
    #         "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
    #     }
    #
    #
    #
    # res = SHOP.shop_update(inf,shopid,imageInfo)
    print(shopid)

