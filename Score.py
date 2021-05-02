bot = int(input("Введите прибыль:"))
usd = int(input("Введите текущий курс Доллара:"))
          
sultan = bot * (66.7 / 100)
malik = bot * (33.3 / 100)
sultanusd= sultan * usd
malikusd = malik * usd
procent_1 = sultanusd * (3.5 / 100)
procent_2 = malikusd * (3.5 / 100)
malik_back = malikusd - procent_2
sultan_back = sultanusd - procent_1 


print("Вы имеете:" , round(sultan),"USD")
print("Вы имеете:", round(malik), "USD")
print("Общий капитал Султана:", round(sultanusd))
print("Общий капитал Малика:", round(malikusd))
print("vosvrat",round(sultan_back),"Rub")
print("vosvrat",round(malik_back),"Rub")
