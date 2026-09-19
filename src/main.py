import random #імпортуємо модуль random для генерації випадкових чисел
import matplotlib.pyplot as plt  # Бібліотека для побудови графіків
import math  # Модуль для використання точного значення числа pi

random.seed(1)  # встановлюємо початкове значення генератора випадкових чисел для відтворюваності результатів

n_values = [10, 100, 1000, 10000, 100000, 1000000] # кількість випробувань для перевірки закону великих чисел
p = 0.5 # теоретична ймовірність випадання події

# Списки для збереження результатів
frequencies = []  # список для збереження відносних частот
errors = []  # список для збереження абсолютних похибок

for N in n_values:
    M = 0

    for _ in range(N):
        r = random.random()  # генеруємо випадкове число від 0 до 1
        if r < p: # перевіряємо, чи випадкове число менше теоретичної ймовірності p
            M += 1  # якщо випадкове число менше p, збільшуємо лічильник успішних випадків
    W = M / N  # обчислюємо відносну частоту випадання події
    delta = abs(W - p)  # обчислення абсолютної похибки

    print("Кількість випробувань: ", N)
    print("Кількість успішних випадків: ", M)
    print("Відносна частота настання події: ",f"{W:.6f}")
    print("Абсолютна похибка: ", f"{delta:.6f}")
    print()
            
    # Зберігаємо результати
    frequencies.append(W)
    errors.append(delta)

# Побудова графіків
plt.plot(n_values, frequencies, marker='o', label="Статистикна частота W(А)")

# Теоретична ймовірність p
plt.axhline(y=p, color='r', linestyle='--', label="Теоретична ймовірність P(A)")
plt.xscale('log')  # Використовуємо логарифмічну шкалу для осі x

#Оформлення графіка
plt.xlabel("Кількість випробувань (N)")
plt.ylabel("Відносна частота W(А)")
plt.title("Закон великих чисел")
plt.legend()
plt.grid(True)

# збереження графіка у файл
plt.savefig("graphics/simulation_results.png")

plt.show()  # Відображення графіка

# Блок 3. Оцінка числа pi методом Монте-Карло

pi_estimates = [] # список для збереження оцінок числа pi
pi_errors = [] # список для збереження абсолютних похибок оцінки числа pi

for N_pi in n_values:
    M_pi = 0

    for _ in range(N_pi):
        x = random.uniform(-1, 1)  # генеруємо випадкове число для координати x
        y = random.uniform(-1, 1)  # генеруємо випадкове число для координати y

        if x**2 + y**2 <= 1:  # перевіряємо, чи точка потрапила в коло
            M_pi += 1  # якщо так, збільшуємо лічильник

    pi_estimate = (M_pi / N_pi) * 4  # оцінка числа pi за формулою
    pi_estimates.append(pi_estimate)

    pi_error = abs(pi_estimate - math.pi)
    pi_errors.append(pi_error)
    print(
    "N =", N_pi,
    "| Оцінка pi:", f"{pi_estimate:.6f}",
    "| Похибка:", f"{pi_error:.6f}"
)

# Побудова графіків для оцінки числа pi
plt.figure()

plt.plot(n_values, pi_estimates, marker='o', label="Оцінка числа pi методом Монте-Карло")
plt.axhline(y=math.pi, color='r', linestyle='--', label="Точне значення числа pi")
plt.xscale('log')  # Використовуємо логарифмічну шкалу для осі x

plt.xlabel("Кількість випробувань (N)")
plt.ylabel("Оцінка числа pi")
plt.title("Оцінка числа pi методом Монте-Карло")
plt.legend()
plt.grid(True)

# збереження графіка у файл
plt.savefig("graphics/pi_estimation.png")
plt.show()  # Відображення графіка

# Блок 4. Комплексна задача, 3 варіант

total_requests = 10000  # загальна кількість запитів
count_2xx = 9700 # кількість запитів з відповіддю 2xx
count_4xx = 200 # кількість запитів з відповіддю 4xx
count_5xx = 100 # кількість запитів з відповіддю 5xx

# Обчислення ймовірностей
P_2xx = count_2xx / total_requests
P_4xx = count_4xx / total_requests
P_5xx = count_5xx / total_requests

# Виведення результатів
print("\nКомплексна задача, 3 варіант:")
print("Ймовірність отримати відповідь 2xx:", f"{P_2xx:.6f}")
print("Ймовірність отримати відповідь 4xx:", f"{P_4xx:.6f}")
print("Ймовірність отримати відповідь 5xx:", f"{P_5xx:.6f}")