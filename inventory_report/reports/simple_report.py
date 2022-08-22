from datetime import datetime
import statistics


class SimpleReport:
    @staticmethod
    def generate(data):
        fabrication_date = sorted(
          data, key=lambda product: product["data_de_fabricacao"]
        )[0]["data_de_fabricacao"]

        sort_by_expiration = sorted(
          data, key=lambda product: product["data_de_validade"]
        )

        today = datetime.today().strftime("%Y-%m-%d")

        for p in sort_by_expiration:
            if p["data_de_validade"] < today:
                sort_by_expiration.remove(p)

        expiration_date = sort_by_expiration[0]["data_de_validade"]

        company_with_most_products = statistics.mode(
          p["nome_da_empresa"] for p in data
        )

        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )
