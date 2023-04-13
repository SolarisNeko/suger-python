from unittest import TestCase

from suger.data_operator import XmlUtils, ElementTree

class TestXmlUtils(TestCase):
    def test_find_element(self):

        # 读取 XML 文件
        xml = XmlUtils('temp/example.xml')

        # 查询节点
        node = xml.find_element('.//book[@id="123"]')
        print(node.text)

        # 修改节点值
        xml.set_element_value('.//book[@id="123"]/name', 'New Book Title')

        # 添加节点
        new_element = ElementTree.Element('book', {'id': '456'})
        sub_element1 = ElementTree.SubElement(new_element, 'name')
        sub_element1.text = 'New Book'
        sub_element2 = ElementTree.SubElement(new_element, 'author')
        sub_element2.text = 'New Author'

        xml.add_element('.//books', new_element)

        # 删除节点
        xml.remove_element('.//book[@id="123"]')

        # 写入文件
        xml.write_file('temp/new_example.xml')

