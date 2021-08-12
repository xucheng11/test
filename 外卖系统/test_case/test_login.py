"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :test_login
# @Date     :2021/8/1 18:26
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import pytest,allure,os,pytest_ordering
from libs.login import  Login
from tools.excel_case import *
@allure.epic("外卖系统")
@allure.feature("登录模块")
@pytest.mark.run(order=3)
class Testlogin:
    @allure.story("登录操作")
    @allure.title("{title}")
    @pytest.mark.parametrize("resBood,resData,title",get_excel("登录模块","Login"))
    # @pytest.mark.parametrize("resBood,resData,title",get_yaml_case("../data/login.yaml"))
    def test_login(self,resBood,resData,title):
        res = Login().login(resBood)
        assert res["msg"]==resData["msg"]

if __name__ == '__main__':
    pytest.main(["test_login.py","--alluredir","../report/tmp","--clean-alluredir"])
    os.system("allure serve ../report/tmp")
