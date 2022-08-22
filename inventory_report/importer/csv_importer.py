from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if ".csv" not in file_path:
            raise ValueError("Arquivo inválido")
        with open(file_path) as file:
            return list(csv.DictReader(file))
