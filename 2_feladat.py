"""
II.
Olvassunk be billentyűzetről tizedes törteket (float), és tároljuk őket egy listában!
A bevitel végét a 0.0 jelzi.
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5.5-nél nagyobb szám a listában?
2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!
3. Hány darab 1 és 2 közé eső szám szerepel a listában?
4. Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?
5. Mennyi a pozitív számok összege?
"""
print("2. feladat")
numbers = []
while True:
    num = float(input("Adj meg egy számot (0.0 a befejezéshez): "))
    if num == 0.0:
        break
    numbers.append(num)

for i in numbers:
    if i > 5.5:
        found = true
        break
if found:
    print("Van 5.5-nél nagyobb szám a listában.")
else:
    print("Nincs 5.5-nél nagyobb szám a listában.")

index_neg_int = -1
for i in range(len(numbers)):
    if numbers[i] < 0 and numbers[i] == int(numbers[i]):
        index_neg_int = i
        break
if index_neg_int != -1:
    print(f"Az első negatív egész szám indexe: {index_neg_int}")
else:
    print("Nincs negatív egész szám a listában.")
