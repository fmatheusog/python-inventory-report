from inventory_report.inventory.product import Product


def test_cria_produto():
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

    assert (product.id) == 1
    assert (product.nome_do_produto) == nome_produto
    assert (product.nome_da_empresa) == nome_empresa
    assert (product.data_de_fabricacao) == data_fabricacao
    assert (product.data_de_validade) == data_validade
    assert (product.numero_de_serie) == numero_serie
    assert (product.instrucoes_de_armazenamento) == instrucoes
