# эта функция проверяет число команд, и на основе этого считает общее кол-во матчей для этих команд. 
# сложность: O(log n).

def numberOfMatches(n: int):
    matches = 0        # задаем переменную для количества матчей.
    while n > 1:        # используем цикл для того, чтобы наши подсчеты велись
			# пока кол-во матчей не достигнет 1.
        if n % 2 != 0:      # условный оператор используем для операций над нашим числом.
            matches += int(n // 2)      # если число нечетное, делим на два и к общему кол-ву матчей 
					# прибавляем 1.
            n = int(n // 2) + 1
        else:
            matches += int(n / 2)       # если же число четно, то просто делим на два и продолжаем дальше.
            n = int(n / 2)
    return matches

print(numberOfMatches(7))