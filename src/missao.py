red_color_code = "\033[91m"
reset_color_code = "\033[0m"

current_battery = input("Carga atual da bateria (em %): ")
current_battery = int(current_battery)
if current_battery < 0 or current_battery > 100:
    print(
        f"{red_color_code}Erro: A carga da bateria deve estar entre 0 e 100%{reset_color_code}"
    )
    exit()

mission_duration = input("Duração da missão (em minutos): ")
mission_duration = int(mission_duration)
if mission_duration < 0:
    print(
        f"{red_color_code}Erro: A duração da missão não pode ser negativa{reset_color_code}"
    )
    exit()

consumption_rate = input("Taxa de consumo da bateria (em % por minuto): ")
consumption_rate = float(consumption_rate)
if consumption_rate < 0:
    print(
        f"{red_color_code}Erro: A taxa de consumo da bateria não pode ser negativa{reset_color_code}"
    )
    exit()

total_consumption = mission_duration * consumption_rate

if current_battery >= total_consumption:
    print("A missão pode ser realizada")
    print(f"Consumo total da missão: {total_consumption}%")
    print(f"Bateria restante: {current_battery - total_consumption}%")
else:
    print("A missão não pode ser realizada")
    print(f"Bateria necessária: {total_consumption}%")
