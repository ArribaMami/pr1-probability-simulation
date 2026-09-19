import random

random.seed(1)

N = 50000  # кількість випробувань

#лічильники для подій
count_A = 0  # лічильник для події A
count_B = 0  # лічильник для події B
count_A_and_B = 0  # лічильник для події A і B
count_A_or_B = 0  # лічильник для події A або B
count_not_A = 0  # лічильник для події не A

for _ in range(N):
    x = random.random()
    y = random.random()

    A = x < 0.5
    B = y < x

    if A:
        count_A += 1
    if B:
        count_B += 1
    if A and B:
        count_A_and_B += 1
    if A or B:
        count_A_or_B += 1
    if not A:
        count_not_A += 1

# Обчислення статистичних ймовірностей
P_A = count_A / N
P_B = count_B / N
P_A_and_B = count_A_and_B / N
P_A_or_B = count_A_or_B / N
P_not_A = count_not_A / N

print("Кількість випробувань N =", N)
print()
print("Статистичні ймовірності:")
print("Статистична P(A):", f"{P_A:.6f}")
print("Статистична P(B):", f"{P_B:.6f}")
print("Статистична P(A ∩ B):", f"{P_A_and_B:.6f}")
print("Статистична P(A ∪ B):", f"{P_A_or_B:.6f}")
print("Статистична P(Ā):", f"{P_not_A:.6f}")

#Теоретичні ймовірності для варіанта 3
P_A_theoretical = 0.5
P_B_theoretical = 0.5
P_A_and_B_theoretical = 0.125
P_A_or_B_theoretical = 0.875
P_not_A_theoretical = 0.5

# Абсолютні похибки
error_A = abs(P_A - P_A_theoretical)
error_B = abs(P_B - P_B_theoretical)
error_A_and_B = abs(P_A_and_B - P_A_and_B_theoretical)
error_A_or_B = abs(P_A_or_B - P_A_or_B_theoretical)
error_not_A = abs(P_not_A - P_not_A_theoretical)

print("Абсолютна похибка P(A):", f"{error_A:.6f}")
print("Абсолютна похибка P(B):", f"{error_B:.6f}")
print("Абсолютна похибка P(A ∩ B):", f"{error_A_and_B:.6f}")
print("Абсолютна похибка P(A ∪ B):", f"{error_A_or_B:.6f}")
print("Абсолютна похибка P(Ā):", f"{error_not_A:.6f}")

# Перевірка властивості протилежної події
print()
print("Перевірка P(Ā) = 1 - P(A):")
print("P(Ā) =", f"{P_not_A:.6f}")
print("1 - P(A) =", f"{1 - P_A:.6f}")

print()
print("Теоретичні ймовірності:")
print("P(A):", f"{P_A_theoretical:.6f}")
print("P(B):", f"{P_B_theoretical:.6f}")
print("P(A ∩ B):", f"{P_A_and_B_theoretical:.6f}")
print("P(A ∪ B):", f"{P_A_or_B_theoretical:.6f}")
print("P(Ā):", f"{P_not_A_theoretical:.6f}")