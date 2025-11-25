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
#Számok felvétele a listába
for i in range(20):
    numbers.append(rn.randint(1,6))
#5-ös dobás
if numbers.count(5) > 0:
    print("Van 5-ös dobás a listában.")
else:
    print("Nincs 5-ös dobás a listában.")
#1-es dobás helye
if numbers.count(1) > 0:
    print(f"{numbers.index(1)}. helyen áll az 1-es szám.")
else:
    print("Nincs 1-ös dobás a listában.")
#Páros számok
for i in numbers:
    if i % 2 == 0:
        even_nums += 1
print(f"{even_nums} páros szám van")
#Legkisebb 4-nél nagyobb
legkisebb = 7
legkisebb_index = -1
for i in range(len(numbers)):
    if numbers[i] > 4:
        if numbers[i] < legkisebb:
            legkisebb = numbers[i]
            legkisebb_index = i

if legkisebb_index != -1:
    print(f"A legkisebb 4-nél nagyobb dobás: {legkisebb} és a(z) {legkisebb_index + 1}. dobás volt.")
else:
    print("Nem volt 4-nél nagyobb dobás.")
#3-asok összege
szumma_3 = 0
for i in range(len(numbers)):
    if numbers[i] == 3:
        szumma_3 += numbers[i]
print(f"A 3-as dobások összege: {szumma_3}")