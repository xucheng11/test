"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :test_shop
# @Date     :2021/8/7 14:19
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import allure,os,pytest,pytest_ordering
from libs.shop import *
from  tools.excel_case import *
@allure.epic("外卖系统")
@allure.feature("我的商铺模块")
@pytest.mark.run(order=2)
class Testshop:
    @allure.story("商铺列表列出操作")
    @allure.title("{title}")
    # @pytest.mark.parametrize("resBood,resData,title",get_excel("我的商铺","listshopping"))
    @pytest.mark.parametrize("resBood,resData,title",get_yaml_case("../data/shop.yaml","listshopping"))
    def test_shop_list(self,resBood,resData,title,shop_init):
        res = shop_init.shop_list(resBood)
        if "code" in res:
            assert res["code"]==resData["code"]
        else:
            assert res["error"]==resData["error"]

    @allure.story("商铺编辑操作")
    @allure.title("{title}")
    @pytest.mark.parametrize("resBood,resData,title",get_excel("我的商铺","updateshopping"))
    def test_shop_update(self,resBood,resData,title,update_shop_init,shop_init):
        res =shop_init.shop_update(resBood,update_shop_init[0],update_shop_init[1])
        assert res["code"]==resData["code"]




if __name__ == '__main__':
    pytest.main(["test_shop.py","--alluredir","../report/tmp","--clean-alluredir","-s"])
    os.system("allure serve ../report/tmp")