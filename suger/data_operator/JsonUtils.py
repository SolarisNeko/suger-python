import json

from suger.common import ObjectUtils


class JsonUtils:
    @staticmethod
    def serialize(obj):
        """Serialize a Python object to a JSON string."""
        if isinstance(obj, (str, int, float, bool, type(None))):
            return json.dumps(obj)
        elif isinstance(obj, (list, tuple)):
            return json.dumps([JsonUtils.serialize(e) for e in obj])
        elif isinstance(obj, dict):
            return json.dumps({k: JsonUtils.serialize(v) for k, v in obj.items()})
        else:
            return json.dumps(vars(obj))

    @staticmethod
    def deserialize(json_str, clazz: type = None):
        """Deserialize a JSON string to a Python object."""
        obj = json.loads(json_str)
        if (ObjectUtils.isNull(clazz)):
            return obj
        return ObjectUtils.dict_to_class(obj, clazz)
