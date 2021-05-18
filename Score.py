bot = int(input("Введите прибыль:"))
usd = int(input("Введите текущий курс Доллара:"))
          
sultan = bot * (60.8 / 100)
malik = bot * (39.2 / 100)
sultanusd= sultan * usd
malikusd = malik * usd
procent_1 = sultanusd * (3.5 / 100)
procent_2 = malikusd * (3.5 / 100)
malik_back = malikusd - procent_2
sultan_back = sultanusd - procent_1
toma = sultan * (11.3 / 100)
tomausd = toma * usd
idar =  sultan * (11.3 / 100)
idarusd = idar * usd
#print("Тома имеет:" , round(toma),"USD")
#print("Идар имеет:" , round(idar),"USD")
print("Султан имеет:" , round(sultan),"USD")
print("Малик имеет:", round(malik), "USD")
#print("Общий капитал Тома:", round(tomausd), "Руб")
#print("Общий капитал Идар:", round(idarusd), "Руб")
print("Общий капитал Султана:", round(sultanusd), "Руб")
print("Общий капитал Малика:", round(malikusd), "Руб")
#print("Возврат с процентами Султан:",round(sultan_back),"Rub") 
#print("Возврат с процентами Малик:",round(malik_back),"Rub")
#print("Купили монетку за 45 USD")
#print("На 02.05.2021 имеем 6925 USD")
