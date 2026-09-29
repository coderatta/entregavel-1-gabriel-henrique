# cores ansi
red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

# pede ao usuario a carga atual
current_battery = input("Carga atual da bateria (em %): ")
current_battery = int(current_battery)
# verifica se ela e invalida, se for mostra o erro e sai do programa
if current_battery < 0 or current_battery > 100:
    print(f"{red}Erro: A carga da bateria deve estar entre 0 e 100%{reset}")
    exit()

# pede ao usuario a duracao da missao
mission_duration = input("Duração da missão (em minutos): ")
mission_duration = int(mission_duration)
# verifica se ela e invalida, se for mostra o erro e sai do programa
if mission_duration < 0:
    print(f"{red}Erro: A duração da missão não pode ser negativa{reset}")
    exit()

# pede ao usuario a taxa de consumo da bateria
consumption_rate = input("Taxa de consumo da bateria (em % por minuto): ")
consumption_rate = float(consumption_rate)
# verifica se ela e invalida, se for mostra o erro e sai do programa
if consumption_rate < 0:
    print(f"{red}Erro: A taxa de consumo da bateria não pode ser negativa{reset}")
    exit()

# calcula o consumo total da missao
total_consumption = mission_duration * consumption_rate

# verifica se a missao pode ser realizada com as condicoes dadas pelo
if current_battery >= total_consumption:
    print(f"\n{green}A missão pode ser realizada{reset}")
    print(f"Consumo total da missão: {total_consumption}%")
    print(f"Bateria restante: {current_battery - total_consumption}%")
else:
    print(f"\n{red}A missão não pode ser realizada{reset}")
    print(f"Bateria necessária: {total_consumption}%")
