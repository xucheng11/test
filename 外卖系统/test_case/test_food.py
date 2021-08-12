"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :test_food
# @Date     :2021/8/8 11:55
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import pytest,os,allure
from tools.excel_case import *

from libs.login import *
from libs.shop import *
from libs.shopping import *
@allure.epic("外卖系统")
@allure.feature("食品管理模块")
@pytest.mark.run(order=1)
class Testfood:
    @pytest.mark.parametrize("resBood,resData,title",get_excel("食品管理","Addfoodkind"))
    @allure.story("食品添加操作")
    @allure.title("{title}")
    def test_food_king(self,resBood,resData,title,food_init,update_shop_init):
        res = food_init.add_shopping_king(resBood,update_shop_init[0])
        if "code" in res:
            assert res["code"]==resData["code"]
        else:
            assert res["error"]==resData["error"]
if __name__ == '__main__':
    pytest.main(["test_food.py", "--alluredir", "../report/tmp", "--clean-alluredir", "-s"])
    os.system("allure serve ../report/tmp")