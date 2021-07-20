from deck_total import Card, Deck

# Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”:

# 1. Создайте колоду из 52 карт. Перемешайте ее.
# 2. Первый игрок берет сверху 6 карт
# 3. Второй игрок берет сверху 6 карт.
# 4. Игрок-1 ходит:
#     1. игрок-1 выкладывает самую маленькую карту по значению
#     2. игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
#     3. Если игрок-2 не может побить карту, то он проигрывает.
#     4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
# 5. Выведите в консоль максимально наглядную визуализацию данного игрового хода.
