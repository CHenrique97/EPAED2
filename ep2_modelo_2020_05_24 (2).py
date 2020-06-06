# -*- coding: UTF-8 -*-
from __future__ import print_function; 
"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP, DECLARO
  QUE SOU O UNICO AUTOR E RESPONSAVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCOES
  DESSE EP E QUE PORTANTO NAO CONSTITUEM DESONESTIDADE ACADEMICA OU PLAGIO.
  DECLARO TAMBEM QUE SOU RESPONSAVEL POR TODAS AS COPIAS DESSE PROGRAMA E
  QUE EU NAO DISTRIBUI OU FACILITEI A SUA DISTRIBUICAO.
  ESTOU CIENTE QUE OS CASOS DE PLAGIO E DESONESTIDADE ACADEMICA SERAO
  TRATADOS SEGUNDO OS CRITERIOS DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome :
  NUSP :
  Turma:
  Prof.:

  Referencias: Com excecao das rotinas fornecidas no enunciado
  e em sala de aula, caso voce tenha utilizado alguma refencia,
  liste-as abaixo para que o seu programa nao seja considerado
  plagio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# Uma vez que as turmas 13 e 14 tem aluno que usa tanto C quanto Python
# nao e' possivel fixar um interpretador e o interpretador Python padrao
# no servidor Linux do e-Disciplinas e' o Python 2. Isso implica diferencas
# na leitura sem quebra de linha ('end=""' abaixo) e o 'raw_input' (no atencao2).

# Manter a linha abaixo para impressao com 'end=""' funcionar no Python 2


"""

EP2 MAC2166 - turma 13 e 14
EP2: sobre polinômios de raizes inteiras ou racionais

ATENCAO2. Algumas opcoes devem ler varias entradas com um unico ENTER,
assim no Python precisa de algum truque e cuidado por tratar-se do Python2.
Para ler a linha inteira usar: linha = raw_input()
Depois deve-se quebrar as entradas usando operador 'split': lista = linha.split()
Entao pode-se pegar cada elemento da 'lista' e tratar como o desejado (e.g.,
convertendo cada elemento para inteiro (funcao 'int(valor)' ou para flutuante
(funcao 'float(valor)').

Pontuacao nas opcoes:
opcao o                                      :  # Testes  | Valor
   o=0 => testa 'avaliaPolinomio'            :   4 testes | 0.61538
   o=1 => testa 'copiaPolinomio'             :   4 testes | 0.61538
   o=2 => testa 'racionalReduzido'           :   5 testes | 0.76923
   o=3 => testa 'polinomioComRaiz'           :   2 testes | 0.30769
   o=4 => testa 'polinomioQuociente'         :  10 testes | 1.5385
   o=5 => testa 'listaCanonicaDeRaizes'      :  25 testes | 3.8462
   o=6 => testa 'polinomioQuocienteRacional' :  15 testes | 2.3077

---
Modelo: verao 2020/05/03

"""

# ======================================================================
# FUNCOES OBRIGATORIAS PRONTAS
# Estas funcoes devem ser utilizadas para simplificar a codificacao em C,
# use-as sem efetuar qualquer alteracao nelas.
# ======================================================================

# ======================================================================
# Usar para lista raizes (para nao gerar problema na avaliacao)
def listaCoeficientes (p) :
  np = len(p);
  print("[ ", end="");
  for i in range(np) :
    print("%f, " % p[i], end="");
  print(" ]");


# ----------------------------------------------------------------------
# Devolve '+' se coef nao eh negativo e existe termo anterior ao
# termo dele no polinomio. Devolve '' (string vazia) no caso
# contrario. Usado para determinar se o '+' deve aparecer antes
# de coef na string que representa o polinomio.
# nTermAnte -- expoente de x no termo anterior ao termo do coef
# coef -- coeficiente de um termo do polinomio
def sig (nTermAnte,coef) :
  if (nTermAnte > 0 and coef >= 0) :
    return "+"
  else:
    return ""


# ----------------------------------------------------------------------
# Devolve uma string que representa o polinomio em um formato legivel.
# Atencao, cuidado com polinomios como "p(x)=-x^2+1" que apos somar 1 torna-se "2" (aqui deve chegar p={1} apenas).
# p -- o vetor dos coeficientes do polinomio
def polinomioToStringF (p) :
  if (p is None) : return "";
  tam = len(p)-1
  expressao = ""
  for m in range(tam-1):
    if (p[tam-m] != 0) :
      expressao = "%s%s%.4fx^%d" % (expressao, sig(m,p[tam-m]), p[tam-m], tam-m);
  if (tam>0 and p[1] != 0) :
    expressao = "%s%s%.4fx" % (expressao, sig(tam-1,p[1]), p[1])
  if (p[0] != 0) :
    expressao = "%s%s%.4f" % (expressao, sig(tam,p[0]), p[0])
  return expressao


# ----------------------------------------------------------------------
# Pode ser usada para conseguir gerar racionais a partir de ponto flutuante.
# Dado um numero flutuante parteFlut, encontra a potencia 'pot' para gerar a
# parte inteira correspondente em 'flutInt'.
# Exemplo: parteFlut=1.020300 => pot=10000, floatInt=10203, ou seja,
#          pot*0.020300 = 10000*0.020300 = 203.00 = floatInt-pot
def encontraInteiro (parteFlut) :
  potA = 1
  if (parteFlut<0) :
    parteFlut = -parteFlut
  while (parteFlut-int(parteFlut) > 0) :
    potA *= 10
    parteFlut *= 10
  return [potA, int(parteFlut)]


# ======================================================================
# FUNCOES ADICIONAIS
# Implemente neste bloco as funcoes adicionais `as obrigatorias do EP2.
# Duas funcoes desse tipo (a polinomioToStringF e a sig) foram
# fornecidas no proprio enunciado do EP.
# ======================================================================

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 

# ======================================================================
# FIM DO BLOCO DE FUNCOES ADICIONAIS
# ======================================================================


# ======================================================================
# FUNCOES OBRIGATORIAS
# Implemente  neste bloco as funcoes obrigatorias do EP2.
# NAO modifique os nomes e parametros dessas funcoes.
# ======================================================================

# Dado o vetor p[] descrevendo um polinomio, avalia-lo em um ponto x dado.
# O valor da avaliacao deve ser devolvido como 'float'.
# Se p(x)=x^2+1, avaliaPolinomio(p,-1.0) devolve 2.0 e avaliaPolinomio(p,2.0) devolve 5.0
# p[] -- coeficientes do polinomio p(x)
# x -- valor no qual deve ser avaliado p(x)
# np -- grau do polinomio p(x)
def avaliaPolinomio (p,x) :
  x=0
  a=0
  b=0
  s=0
  p[0]=int(x)
  return (x*p[1]+p[0])

# ----------------------------------------------------------------------
# Fazer a copia de um polinomio dado.
# p1[] -- coeficientes do polinomio p1(x)
# p2[] -- coeficientes do polinomio com a copia de p1(x)
def copiaPolinomio (p1, p2) :
  for x in p1:
    p2.append(x)
  # Implemente aqui a funcao...

# ----------------------------------------------------------------------
# Dados inteiros valores representando racional b/a, obter a forma reduzida de b/a
# Se b/a=15/3 devolve 5/1
# b -- inteiro para numerador
# a -- inteiro para denominador
def reduzRacional (b, a) :
  d = gcd(b, a) 
  
  b = b // d 
  a = a // d 
  
  return (str(int(b))+'/'+str(int(a)))
  # Implemente aqui a funcao...


# ----------------------------------------------------------------------
# Devolve uma string que apresenta a raiz r do polinomio na forma racional
# reduzida (e.g. 0.5 devolve "1/2", 6/8 devolve "3/4")
# Usar funcao 'reduzRacional'
# r -- uma raiz do polinomio
def racionalReduzido (r) :
  rRed=r*100000
  formaFinal=reduzRacional(rRed,100000)
  return formaFinal


# ----------------------------------------------------------------------
# Devolve 1 se b eh raiz do polinomio representado pela lista p e 0 em caso contrario.
# p -- a lista dos coeficientes do polinomio
# b -- o numero a ser testado como raiz
def polinomioComRaiz (p,b) :
  print()
  # Implemente aqui a funcao...


# ----------------------------------------------------------------------
# Devolve a lista que representa o polinomio quociente da divisao
# p(x)/(x-b), onde p(x) eh o polinomio cujos coeficientes estao na
# lista p e b eh uma raiz de p(x).
# p -- a lista dos coeficientes do polinomio a ser dividido
def polinomioQuociente (p,b):
  print()
  # Implemente aqui a funcao...


# ----------------------------------------------------------------------
# Devolve a lista canonica de raizes inteiras do polinomio
# representado pela lista p.
# p -- a lista dos coeficientes do polinomios
def listaCanonicaDeRaizes (p):
  print()
  # Implemente aqui a funcao...

# ----------------------------------------------------------------------
# Devolve a lista que representa o polinomio quociente da divisao
# p(x)/(ax-b) e o resto dessa divisao, onde p(x) eh o polinomio
# cujos coeficientes estao na lista p e b/a eh uma raiz de p(x).
# p -- a lista dos coeficientes do polinomio a ser dividido
# b -- numerador da raiz a ser usada como divisor
# a -- denominador da raiz a ser usada como divisor
def polinomioQuocienteRacional (p,b,a) :
  print()
  # Implemente aqui a funcao...



# ======================================================================
# FIM DO BLOCO DE FUNCOES OBRIGATORIAS
# ======================================================================


# ======================================================================
# INICIO DO BLOCO DE FUNCOESPARA EXECUTAR CADA OPCAO
# ======================================================================

# Implementar aqui as 7 funcoes para cada opcao (0 ate' 6).

# ======================================================================
# FIM DO BLOCO DE FUNCOES PARA EXECUTAR CADA OPCAO
# ======================================================================
2

# ======================================================================
# FUNCAO MAIN
# Escreva dentro da funcao main() o codigo que quiser para testar suas demais funcoes.
# Somente dentro da funcao main() e funcoes de opcao voce pode usar as funcoes print ou input.
# O codigo da funcao main() NAO sera avaliado.
# ======================================================================
def main () :
  print("Digite opcao:"),    
  selectOpt=input()
  if (selectOpt==0):
    print()
  if (selectOpt==1):
    print()
  if (selectOpt==2):
    print("Digite os 5 valores:")
    numero=raw_input()
    numeroList=numero.split()
    for x in numeroList:
     #print(x)
     print(racionalReduzido(float(x)))

  if (selectOpt==3):
    print()
  if (selectOpt==4):
    print()
  if (selectOpt==5):
    print()
  if (selectOpt==6):
    print()
  # Implemente aqui a funcao...

# ======================================================================
# FIM DA FUNCAO MAIN
# ======================================================================


# ======================================================================
# CHAMADA DA FUNCAO MAIN
# NAO modifique os comandos deste bloco!
# ======================================================================

if __name__ == "__main__":
  main()

# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNCAO MAIN
# ======================================================================
