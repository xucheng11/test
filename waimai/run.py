"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :run
# @Date     :2021/8/7 15:09
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import pytest,os
if __name__ == '__main__':
    pytest.main(["test_case", "--alluredir", "report/tmp", "--clean-alluredir", "-s"])
    os.system("allure serve report/tmp")