from unittest import TestCase

from suger.data_operator.ExcelUtils import ExcelUtils


class TestExcelUtils(TestCase):

    def test_serialize(self):
        # 读取 Excel 文件
        workbook = ExcelUtils.load_workbook("example.xlsx")

        # 获取指定名称的 sheet 对象
        sheet = ExcelUtils.get_sheet_by_name(workbook, "Sheet1")

        # 将 sheet 序列化为一个列表
        data = ExcelUtils.serialize(sheet, skip_rows=1)

        # 对列表进行操作

        # 反序列化列表到指定的 sheet 对象
        ExcelUtils.deserialize(sheet, data, skip_rows=1)

        # 保存 Excel 文件
        ExcelUtils.save_workbook(workbook, "example.xlsx")
