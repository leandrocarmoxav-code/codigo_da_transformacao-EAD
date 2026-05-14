from datetime import datetime

agora = datetime.now()

print("Data atual:", agora.strftime("%Y-%m-%d"))
print("Hora atual:", agora.strftime("%H:%M:%S"))