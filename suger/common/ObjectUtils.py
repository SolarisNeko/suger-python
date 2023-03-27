
# @author SolarisNeko
class ObjectUtils:

    @staticmethod
    def isNull(obj) -> bool:
        return obj is None

    @staticmethod
    def isNotNull(obj) -> bool:
        return not (obj is None)

    @staticmethod
    def defaultIfNull(obj, defaultObj) -> object:
        """
        如果 obj 为 None，则返回 default；否则返回 obj。
        """
        return defaultObj if obj is None else obj

    @staticmethod
    def equals(obj1, obj2) -> bool:
        """
        判断 obj1 是否等于 obj2，如果 obj1 和 obj2 均为 None，则返回 True。
        """
        if obj1 is None and obj2 is None:
            return True
        elif obj1 is None or obj2 is None:
            return False
        else:
            return obj1 == obj2

    @staticmethod
    def hashCode(obj) -> int:
        """
        返回 obj 的哈希值，如果 obj 为 None，则返回 0。
        """
        return 0 if obj is None else hash(obj)
