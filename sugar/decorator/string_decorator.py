def string(clazz):
    '''
    根绝 field 自动生成 class 的 __str__
    :param clazz: 类
    :return: clazz
    '''
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
    clazz.__str__ = __str__
    return clazz

