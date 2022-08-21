from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_produto = "nome_produto"
    nome_empresa = "nome_empresa"
    data_fabricacao = "data_fabricacao"
    data_validade = "data_validade"
    numero_serie = "numero_serie"
    instrucoes = "instrucoes"

    product = Product(
        id,
        nome_produto,
        nome_empresa,
        data_fabricacao,
        data_validade,
        numero_serie,
        instrucoes
        )

    assert (repr(product)) == (
        f"O produto {nome_produto}"
        f" fabricado em {data_fabricacao}"
        f" por {nome_empresa} com validade"
        f" até {data_validade}"
        f" precisa ser armazenado {instrucoes}."
    )
