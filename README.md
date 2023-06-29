# suger

version = 0.2.1

## Introduce 介绍

suger is a sugar ~ 

use python with @decorator/@Annotation Like Java、C#、TypeScript 

@author SolarisNeko


# What is it
Use Python in Decorator / Annotation Like Java Lombok / C# Annotation / TypeScript Decorator

作者是写 Java / TypeScript 习惯了注解

Use Like Other Language:
1. Java Lombok @Data
2. TypeScript  @Async
3. C#  [Required(ErrorMessage = "{0} is required")]

顺手写

# How to use 如何使用
## install 安装依赖
```shell
pip install suger
```

## Stream 流式计算 / from v0.2.1 
```python
from suger.stream.Stream import Stream

    def test_demo(self):
        data = [1, 2, 3, 3, 4, 5]
        result = Stream(data).filter(lambda x: x % 2 == 0) \
            .sort(reverse=True) \
            .map(lambda x: x * 2) \
            .toSet()
        self.assertEqual(result, {8, 4})

```

## decorator 装饰器/注解
### @string | __str__
```python
@string
class MockData:
    def __init__(self, age):
        self.age = age


data = MockData(18)

# Output = "MockData(age=18)"
print(data)

```

### @csv | CSV 
```python
@csv
class MockData:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.emptyTips = ''




class Test(TestCase):
    def test_csv(self):
        data = MockData(name='neko', age=18)

        # csv 输出文本
        print(data.csv_str())
        # csv 的格式
        print(data.csv_format())

# 示例中，有个字段为空
# neko,18,
# name,age,emptyTips

```

## 工具
### FileUtils 文件工具
```python

from suger.common import FileUtils

# 递归扫描, png 格式
fileArray = FileUtils.scanDir('C:/Users/suger/Documents/WeChat Files', 'png')
print(fileArray)

```


### ObjectUtils 对象工具
```python
from suger.common import ObjectUtils

# true
ObjectUtils.isNull(None)

#  true
data = {}
ObjectUtils.isNotNull(data)



```

## SSH
```python
from unittest import TestCase

from suger.terminal import SSH


class TestSSH(TestCase):
    def test_connect(self):
        ssh = SSH(host='localhost', password='root')
        ssh.connect()
        output, err = ssh.execute_command('ls .')
        print(output)


```

## Data Operator 数据操作
### XML
```python
from unittest import TestCase

from suger.data_operator import XmlUtils, ElementTree

class TestXmlUtils(TestCase):
    def test_find_element(self):

        # 读取 XML 文件
        xml = XmlUtils('example.xml')

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
        xml.write_file('new_example.xml')


```


### Excel 
```python
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

```


# my project init
```shell
git init

 git remote add github https://github.com/SolarisNeko/neko233-python-suger.git
 git remote add origin https://gitee.com/SolarisNeko/neko233-python-suger.git
```
