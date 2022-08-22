from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        complete_report = SimpleReport.generate(data)
        complete_report += "\nProdutos estocados por empresa:\n"

        companies = Counter(
          p["nome_da_empresa"] for p in data
          if p.get("nome_da_empresa")
        )

        for key, value in companies.items():
            complete_report += f"- {key}: {value}\n"

        return complete_report
