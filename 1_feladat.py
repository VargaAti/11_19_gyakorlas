"""
I.
Szimuláljuk egy 6 oldalú kocka 20 dobását! A dobásokat egy listában tároljuk!
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5-ös dobás a listában?
2. Hanyadik dobás lett először 1-es?
3. Hány darab páros számot dobtunk?
4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?
5. Mennyi a 3-as dobások összege?
"""
import random as rn
print("1. feladat")
numbers = []
even_nums = 0
for i in range(21):
    numbers.append(rn.randint(1,20))
if numbers.count(5) > 0:
    print("Van 5-ös dobás a listában.")
if numbers.count(1) > 0:
    print(f"{numbers.index(1)}. helyen áll az 1-es szám.")
for i in numbers:
    if i % 2 == 0:
        even_nums += 1
print(f"{even_nums} páros szám van")
