def csv(clazz):
    '''
    根绝 field 自动生成 csv, 赋值到 class 的 __str__ 来输出
    :param clazz: 类
    :return: clazz
    '''

    def csv_str(self):
        return '%s' % (
            ','.join(
                # 元组 (key, value)
                '%s' % item[1] for item in vars(self).items()
            )
        )

    def csv_format(self):
        return '%s' % (
            ','.join(
                '%s' % item[0] for item in vars(self).items()
            )
        )

    clazz.csv_str = csv_str
    clazz.csv_format = csv_format

    return clazz
