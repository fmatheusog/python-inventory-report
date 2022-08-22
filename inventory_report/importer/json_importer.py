from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if ".json" not in file_path:
            raise ValueError("Arquivo inválido")
        with open(file_path) as file:
            return json.loads(file.read())
