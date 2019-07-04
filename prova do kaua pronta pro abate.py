# Avaliação de Programação
# Resolva esses exercícios sem usar if, for ou while.
# Utilize apenas fatiamento, funções embutidas e métodos dos
# objetos string, lista, dicionário, etc.

def soma_tres_inteiros(a, b, c):
    """ Recebe três números inteiros, e retorna a sua soma"""
    return a + b + c

def preco_com_desconto(preco, percentual):
    """ Recebe um preço e sua porcentagem de desconto, e retorna
    novo preço"""

    newprice  = (preco*percentual)/100
    preco_com_desconto = round( preco -newprice ,2)
    return preco_com_desconto


def aluguel_airbnb(valor_diaria, dias):
    """ Recebe uma quantidade de dias que ficou hospedado e o valor da
    diária, e retorna o valor a ser pago, considerando um acréscimo de
    R$ 75,00 para limpeza e 5% de taxa de administração sobre o valor
    do aluguel sem a taxa de limpeza"""

    total = valor_diaria*dias
    a =  (total/100) * 5

    return (total + a) + 75

def media_final_aprovado_reprovado(prova, exercicio, projeto):
    """ Recebe as notas de 1 prova, 1 exercício e 1 projeto, e retorna
    se o aluno foi ou não aprovado. A prova tem peso 4, o exercício
    tem peso 1, e o projeto tem peso 3."""


    a = prova * 4 / 10
    b = exercicio / 10
    c = projeto * 3 / 10
    return a + b + c >= 5.6


def troca_caixa(texto):
    """Vogais ficam em caixa baixa (minúsculas)
    Consoantes ficam em caixa alta (maiúsculas)"""

    texto = texto.upper()
    texto = texto.replace('A', 'a')
    texto = texto.replace('E', 'e')
    texto = texto.replace('I', 'i')
    texto = texto.replace('O', 'o')
    texto = texto.replace('U', 'u')
    return texto


    return texto


def encontra_caracter(texto, caracter_procurado):
    """Receba um texto e retorne a localização da primeira vez que
    aparece o caracter especificado"""

    pega_pega = texto.find(caracter_procurado)
    return pega_pega

def é_sortudo(numero):
    """O último dígito deve ser igual ao primeiro, e ao elemento do meio."""

    parte1 = len(numero)
    metade = parte1 / 2
    inteiro = int(metade)
    primeiro = numero[0]
    ultimo = numero[-1]
    meio = numero[inteiro]
    return primeiro ==meio==ultimo






def media_saltos_lista(saltos):
    """Receba uma lista com os saltos de um atleta e calcule a média
    dos seus saltos.
    """
    return (sum(saltos)) / (len(saltos))


def mes_extenso(mes):
    """Receba um número correspondente ao mês e devolva o nome do mês.
    Ex.: 1-janeiro, 2-fevereiro, ..., 12-dezembro.
    Use um dicionário com os nomes dos meses."""

    de_novo_isso_sor = {1:'janeiro',
           2:'fevereiro',
           3:"março",
           4:"abril",
           5:"maio",
           6:"julho",
           7:"junho",
           8:"agosto",
           9:"setembro",
           10:"outubro",
           11:"novembro",
           12:"dezembro"}
    return de_novo_isso_sor[mes]
def insere(texto, posicao, texto_inserir):
    """
    Insira na posição especificada o novo texto.
    """

    return texto[0:posicao] + texto_inserir + texto[posicao:]






# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % 'Falhou'
    else:
        prefixo = '\033[32m%s' % 'Passou'
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():

    print('Soma três inteiros:')
    test(soma_tres_inteiros(0, 0, 0), 0)
    test(soma_tres_inteiros(-1, 0, 0), -1)
    test(soma_tres_inteiros(10, 10, 10), 30)
    test(soma_tres_inteiros(-10, -10, -10), -30)

    print('Desconto do preco atual baseado na porcentagem do desconto:')
    test(preco_com_desconto(1330, 20), 1064.00)
    test(preco_com_desconto(1000, 0), 1000.00)
    test(preco_com_desconto(1000.10, 5.5), 945.09)
    test(preco_com_desconto(0.0, 200), 0.00)

    print('Preco a pagar pelo aluguel do airBnB:')
    test(aluguel_airbnb(100, 1), 180.00)
    test(aluguel_airbnb(100, 2), 285.00)
    test(aluguel_airbnb(200, 10), 2175.00)
    test(aluguel_airbnb(50, 5), 337.50)

    print('Média final:')
    test(media_final_aprovado_reprovado(10, 10, 10), True)
    test(media_final_aprovado_reprovado(8, 7, 6), True)
    test(media_final_aprovado_reprovado(8, 7, 5), False)
    test(media_final_aprovado_reprovado(5, 5, 5), False)
    test(media_final_aprovado_reprovado(7, 7, 7), True)

    print(' Troca caixa:')
    test(troca_caixa("Araquari"), "aRaQuaRi")  # normal
    test(troca_caixa("Caxias do Sul"), "CaXiaS Do SuL")  # com espaços

    print(' Encontra caracter:')
    test(encontra_caracter("--*--", "*"), 2)
    test(encontra_caracter("19/05/2014", "/"), 2)
    test(encontra_caracter("Avaliação de Programação", "P"), 13)

    print(' É sortudo:')
    test(é_sortudo('2132452'), True)
    test(é_sortudo('23141'), False)
    test(é_sortudo('31213145563'), False)
    test(é_sortudo('3455133453341'), False)
    test(é_sortudo('3455133453343'), True)

    print(' Média dos saltos em lista:')
    test(media_saltos_lista([10, 10, 10, 10, 10]), 10)
    test(media_saltos_lista([9, 9.1, 8, 7, 6.9]), 8)
    test(media_saltos_lista([1, 1, 3, 5, 5]), 3)
    test(media_saltos_lista([10, 10, 9.9, 10, 10]), 9.98)
    test(media_saltos_lista([1, 4.5, 0, 7, 5]), 3.5)

    print('Mês por extenso:')
    test(mes_extenso(1), 'janeiro')
    test(mes_extenso(3), 'março')
    test(mes_extenso(12), 'dezembro')

    print('Apaga')
    test(insere('kitten', 3, 'i'), 'kititen')
    test(insere('nasci', 2, 'i'), 'naisci')
    test(insere('code', 0, 'vs'), 'vscode')
    test(insere('code', 1, 'h'), 'chode')
    test(insere('chocolate', 9, 's'), 'chocolates')


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total)
          )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
