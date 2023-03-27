# sugar

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
pip install sugar
```

## @string | __str__
```python
@string
class MockData:
    def __init__(self, age):
        self.age = age


data = MockData(18)

# Output = "MockData(age=18)"
print(data)

```

## @csv | CSV 
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


# my project init
```shell
git init

 git remote add github https://github.com/SolarisNeko/neko233-python-sugar.git
 git remote add origin https://gitee.com/SolarisNeko/neko233-python-sugar.git
```
