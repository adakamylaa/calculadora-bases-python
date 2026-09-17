"""Calculadora de conversão entre as bases Decimal, Binária, Octal e Hexadecimal."""


BASES = {
    "1": ("Decimal", 10),
    "2": ("Binária", 2),
    "3": ("Octal", 8),
    "4": ("Hexadecimal", 16),
}


def exibir_menu():
    """Exibe as opções disponíveis e retorna a escolha do usuário."""
    print("\n=== Calculadora de Bases ===")
    print("1 - Decimal")
    print("2 - Binária")
    print("3 - Octal")
    print("4 - Hexadecimal")
    print("0 - Sair")
    return input("Escolha a base de origem: ").strip()


def obter_digitos_validos(base):
    """Retorna os caracteres permitidos para uma determinada base."""
    if base == 2:
        return "01"
    if base == 8:
        return "01234567"
    if base == 10:
        return "0123456789"
    return "0123456789abcdefABCDEF"


def valor_valido(valor, base):
    """Verifica se o valor informado é válido para a base escolhida."""
    valor = valor.strip()
    if not valor:
        return False

    # Sinais podem aparecer somente no início do número.
    if valor[0] in "+-":
        valor = valor[1:]

    if not valor:
        return False

    digitos_validos = obter_digitos_validos(base)
    return all(digito in digitos_validos for digito in valor)


def converter_para_decimal(valor, base):
    """Converte um valor da base escolhida para um inteiro decimal."""
    return int(valor.strip(), base)


def formatar_conversoes(numero):
    """Formata o número inteiro nas quatro bases."""
    return {
        "Decimal": str(numero),
        "Binária": format(numero, "b"),
        "Octal": format(numero, "o"),
        "Hexadecimal": format(numero, "X"),
    }


def exibir_resultados(numero):
    """Exibe o valor convertido em todas as bases."""
    conversoes = formatar_conversoes(numero)
    print("\n--- Resultado ---")
    for nome_base, valor in conversoes.items():
        print(f"{nome_base:12}: {valor}")


def solicitar_valor(nome_base, base):
    """Solicita um valor até que ele seja válido para a base informada."""
    while True:
        valor = input(f"Informe o valor em {nome_base}: ").strip()
        if valor_valido(valor, base):
            return valor
        print(f"Erro: '{valor}' não é um número válido na base {base}.")


def main():
    """Executa o loop principal da calculadora."""
    while True:
        escolha = exibir_menu()

        if escolha == "0":
            print("Programa encerrado.")
            break

        if escolha not in BASES:
            print("Erro: escolha uma opção entre 0 e 4.")
            continue

        nome_base, base = BASES[escolha]
        valor = solicitar_valor(nome_base, base)
        numero = converter_para_decimal(valor, base)
        exibir_resultados(numero)


if __name__ == "__main__":
    main()