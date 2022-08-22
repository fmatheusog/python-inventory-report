from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if ".xml" not in file_path:
            raise ValueError("Arquivo inválido")
        with open(file_path) as file:
            data = file.read()
            xml = xmltodict.parse(data)
            return xml["dataset"]["record"]
