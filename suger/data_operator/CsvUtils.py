import csv
import io


class CsvUtils:
    @staticmethod
    def serialize(obj):
        """Serialize a Python object to a CSV string."""
        if isinstance(obj, list):
            if len(obj) == 0:
                return ''
            csv_file = io.StringIO()
            writer = csv.writer(csv_file)
            writer.writerow(obj[0].__dict__.keys())
            for item in obj:
                writer.writerow(item.__dict__.values())
            return csv_file.getvalue()
        else:
            fieldnames = obj.__dict__.keys()
            csv_file = io.StringIO()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(obj.__dict__)
            return csv_file.getvalue()

    @staticmethod
    def deserialize(csv_str, obj_class):
        """Deserialize a CSV string to a Python object."""
        if not csv_str:
            return None
        if '\n' in csv_str:
            reader = csv.DictReader(io.StringIO(csv_str))
            result = []
            for row in reader:
                result.append(obj_class(**row))
            return result
        else:
            reader = csv.DictReader(io.StringIO(csv_str))
            obj_dict = next(reader)
            obj = obj_class(**obj_dict)
            return obj
