# entregavel-1-gabriel-henrique

>Entregável da primeira semana do processo seletiva da <span style="color:#A040FF">UFRJ Harpia<span>

**Autor:** Gabriel Henrique Freitas Ribeiro

## Descrição:
Um programa simples que calcula se a missão de um robô pode ser realizada sabendo-se a bateria inicial, a duração da missão e a taxa de descarregamento(considerada constante)

O programa pede essas informações e verifica se os valores são válidos e calcula o gasto de bateria ao final da missão. Se houver bateria o bastante ele retorna o consumo total e a bateria restante, se nao for o suficiente ele retorna a bateria necessária para o tempo da missão.

## Execução:

Usando o comando `python3 src/missao.py` a partir do diretório principal, o programa pedirá os valores um por um e devolver um veredito

Exemplos de uso:

## 💻 Exemplos de Uso

### Com sucesso
```text
Carga atual da bateria (em %): 70
Duração da missão (em minutos): 20
Taxa de consumo da bateria (em % por minuto): 3

A missão pode ser realizada
Consumo total da missão: 60.0%
Bateria restante: 10.0%
```
### Sem sucesso
```text
Carga atual da bateria (em %): 40
Duração da missão (em minutos): 15
Taxa de consumo da bateria (em % por minuto): 4

A missão não pode ser realizada
Bateria necessária: 60.0%
```

