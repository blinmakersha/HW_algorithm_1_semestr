# эта функция проверяет, является ли камень драгоценным. сложность: O(n2).

def numJewelsInStones(jewels: str, stones: str):
  result = 0
  for jewel in jewels:      # создаем цикл, который проходится по каждому элементу в драгоценностях
    for stone in stones:        # создаем цикл, который проходит по каждому элементу в камнях
      if jewel == stone:        # через условный оператор проверяем каждый элемент в камнях на наличие 
драгоценности
        result += 1
  return result

print(numJewelsInStones("B", "aAAbbbb"))
