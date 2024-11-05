from collections import defaultdict

# Função principal
def analisar_vendas(vendas):
    # Dicionários para armazenar os dados
    contagem_vendas = defaultdict(int)  # Contagem de vendas por produto
    receita_acumulada = defaultdict(float)  # Receita acumulada por produto
    soma_vendas_diarias = defaultdict(float)  # Soma das vendas diárias por produto
    dias_venda = defaultdict(set)  # Para registrar os dias únicos de vendas de cada produto

    # Processar cada venda
    for produto, quantidade, preco_unitario, dia in vendas:
        # Atualizando a contagem de vendas
        contagem_vendas[produto] += quantidade
        
        # Atualizando a receita acumulada
        receita_acumulada[produto] += quantidade * preco_unitario
        
        # Atualizando a soma das vendas diárias
        soma_vendas_diarias[produto] += quantidade
        
        # Registrando o dia da venda (usado para calcular a média diária)
        dias_venda[produto].add(dia)
    
    # Exibindo os resultados
    for produto in contagem_vendas:
        contagem = contagem_vendas[produto]
        receita = receita_acumulada[produto]
        soma_diarias = soma_vendas_diarias[produto]
        dias_unicos = len(dias_venda[produto])
        
        # Calculando a média de vendas diárias
        if dias_unicos > 0:
            media_diarias = soma_diarias / dias_unicos
        else:
            media_diarias = 0
        
        # Exibindo as informações detalhadas
        print(f"Produto: {produto}")
        print(f"  Contagem de vendas: {contagem}")
        print(f"  Receita acumulada: R${receita:.2f}")
        print(f"  Média de vendas diárias: {media_diarias:.2f}")
        print()

# Exemplo de entrada (lista de tuplas)
vendas = [
    ('Produto A', 10, 30.0, '2024-11-01'),
    ('Produto A', 5, 30.0, '2024-11-02'),
    ('Produto B', 8, 15.0, '2024-11-01'),
    ('Produto A', 3, 30.0, '2024-11-02'),
    ('Produto B', 12, 15.0, '2024-11-03'),
    ('Produto A', 7, 30.0, '2024-11-03'),
]

# Executando a análise
analisar_vendas(vendas)









