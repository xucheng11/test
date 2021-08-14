"""
-------------------------------------------------
# @Project  :外卖系统
# @File     :excel_case
# @Date     :2021/8/1 18:06
# @Author   :小成
# @Email    :1224069978
# @Software :PyCharm
-------------------------------------------------
"""
import xlrd,json,pprint,yaml
#处理excel用例封装
def get_excel(sheetName,caseName):
    rilist= []
    url = "../data/Delivery_System_excel-V1.5.xls"
    workbook = xlrd.open_workbook(url,formatting_info=True)
    worksheet = workbook.sheet_by_name(sheetName)
    inx = 0
    for one in worksheet.col_values(0):
        if caseName in one:
            resboodData = worksheet.cell_value(inx,9)
            resData = worksheet.cell_value(inx,11)
            biaoti = worksheet.cell_value(inx,4)
            rilist.append((json.loads(resboodData),json.loads(resData),biaoti))
        inx += 1

    return rilist

#处理yaml用例数据封装
def get_yaml_case(fileDir,casename):
    rilst =[]
    fo = open(fileDir,"r",encoding="utf-8")
    res = yaml.load(fo,Loader=yaml.FullLoader)
    for one in res:
        if casename in one["test"]:
            rilst.append((one["data"],one["resp"],one["biaoti"]))
    return rilst



if __name__ == '__main__':
    pprint.pprint(get_yaml_case("../data/shop.yaml","updateshopping"))
    # print("-----------")
    # pprint.pprint(get_excel("我的商铺","listshopping"))
