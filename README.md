# ESTAGIO-RP
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
          RESPOSTA: 
  def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Exemplo de uso
n = 10  # Número de termos
print(fibonacci(n))


2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
          def contar_letra_a(texto):
    # Convertendo o texto para minúsculas para verificar 'a' e 'A'
    texto = texto.lower()
    
    # Contando a ocorrência da letra 'a'
    quantidade_a = texto.count('a')
    
    # Verificando se a letra 'a' existe
    if quantidade_a > 0:
    
        print (f"A letra 'a' (maiúscula ou minúscula) aparece {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Exemplo de uso
texto = input("Digite uma string: ")
contar_letra_a(texto)



3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
     
Ao final do processamento, qual será o valor da variável SOMA?
              RESPOSTA: SOMA = 77   (CODIGO ABAIXO, TESTADO EM VSCODE)
INDICE = 12
SOMA = 0
K = 1
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

# Imprimindo o resultado
print(SOMA)
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, 9___
b) 2, 4, 8, 16, 32, 64, _128___
c) 0, 1, 4, 9, 16, 25, 36, _49___
d) 4, 16, 36, 64, _100___
e) 1, 1, 2, 3, 5, 8, _13___
f) 2,10, 12, 16, 17, 18, 19, _20___



5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
              RESPOSTA:  LIGARIA UM INTERRUPTOR E ESPERARIA ALGUNS MINUTOS, DEPOIS DESLIGARIA O MESMO INTERRUPTOR E LIGARIA OUTRO, EM SEGUIDA IRIA VER AS SALAS. NA SALA QUE ESTIVER DESLIGADA E QUENTE CORRESPONDE AO PRIMEIRO INTERRUPTOR LIGADO. A LAMPADA ACESA, AO SEGUNDO INTERRUPTOR LIGADO E A ULTIMA LAMPADA AO ULTIMO INTERRUPTOR.
   
