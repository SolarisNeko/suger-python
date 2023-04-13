import xml.etree.ElementTree as ElementTree


class XmlUtils:

    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = ElementTree.parse(self.file_path)
        self.root = self.tree.getroot()

    def find_element(self, element_path):
        return self.root.find(element_path)

    def find_elements(self, element_path):
        return self.root.findall(element_path)

    def set_element_value(self, element_path, value):
        element = self.find_element(element_path)
        element.text = str(value)
        self.tree.write(self.file_path)

    def add_element(self, element_path, element):
        parent = self.find_element(element_path)
        parent.append(element)
        self.tree.write(self.file_path)

    def remove_element(self, element_path):
        parent = self.find_element(element_path)
        parent.clear()
        self.tree.write(self.file_path)

    def write_file(self, file_path=None):
        if file_path:
            self.tree.write(file_path)
        else:
            self.tree.write(self.file_path)
