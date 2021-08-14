"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :conftest
# @Date     :2021/8/7 14:04
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
from libs.login import *
from libs.shop import *
from conf.host import *
from libs.shopping import *
import pytest,allure
@pytest.fixture(scope="session")
def login_init1():
    token = Login().login(user,getToken=True)
    return token

#商品店铺登录前置操作
@pytest.fixture(scope="class")
def shop_init(login_init1):
    shop=Shop(login_init1)
    return shop
a ={
            "name": "星巴克新建店",
            "address": "上海市静安区秣陵路303号",
            "id": "3269",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }
#商铺编辑前置条件
@allure.story("编辑商铺前置条件")
@pytest.fixture(scope="class")
def update_shop_init(shop_init):
    print("---正在数据初始化")
    shopid = shop_init.shop_list({"page":1,"limit":1})['data']['records'][0]['id']
    imageInfo =shop_init.shop_file("aaa.png","data/aaa.png")
    yield shopid,imageInfo
    #恢复原先数据
    print("---正在操作数恢复")
    imageInfo1 = shop_init.shop_file("bbb.png", "data/bbb.png")
    res = shop_init.shop_update(a,shopid,imageInfo1)

#食品添加前置条件
@pytest.fixture(scope="class")
def food_init(login_init1):
    food= shopping(login_init1)
    return food





