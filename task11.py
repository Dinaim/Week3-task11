# 5)Напишите функцию которая принимает: день, месяц, год
# и возвращает 'True' если такая дата есть, если нет то 'False'

def date(day, month, year):
        if month > 0 and month <= 12: ## If month is between 1 and 12, return True.
            return True
        else:
            return False

print(date(12, 12, 2030))