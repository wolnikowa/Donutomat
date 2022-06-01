from random import choices, randint, randrange, random
from functools import partial
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time
import numpy as np

# problem sat3

# funkcja fitness
def fitness(genome, formulas):
    sum_f = 0
    for formula in formulas:
        for cla in formula:
            for el in cla:
                number_of_variable = el["x_n"]
                value_of_variable = genome[number_of_variable] #sprawdzam czy genom[x_n] równa sie 0 czy 1 (0=f or 1=t)
                # jesli wartość jest negatywna to zmieniam "wynik" na odwrotny
                # print(el,genome,value_of_variable)
                if el["negative"] == 1:
                    value_of_variable = abs(value_of_variable - 1)
                #     jesli wynik jest true to dodaje 1 do sum_f (bo wystarczy nam conajmniej 1 w nawiasie aby cały był true
                if value_of_variable == 1:
                    sum_f += 1
                    break
    # sum_f zwraca ile jest poprawnych nawiasów
    return sum_f
# przykładowa "formulas":
# [[[{'x_n': 24, 'negative': 0}, {'x_n': 26, 'negative': 1}, {'x_n': 27, 'negative': 0}], [{'x_n': 20, 'negative': 0}, {'x_n': 12, 'negative': 1}, {'x_n': 2, 'negative': 1}], [{'x_n': 11, 'negative': 1}, {'x_n': 0, 'negative': 0}, {'x_n': 12, 'negative': 0}], [{'x_n': 11, 'negative': 1}, {'x_n': 18, 'negative': 1}, {'x_n': 19, 'negative': 1}], [{'x_n': 12, 'negative': 1}, {'x_n': 17, 'negative': 1}, {'x_n': 21, 'negative': 0}], [{'x_n': 22, 'negative': 1}, {'x_n': 2, 'negative': 0}, {'x_n': 8, 'negative': 1}], [{'x_n': 26, 'negative': 0}, {'x_n': 5, 'negative': 1}, {'x_n': 12, 'negative': 0}], [{'x_n': 4, 'negative': 1}, {'x_n': 18, 'negative': 1}, {'x_n': 19, 'negative': 0}], [{'x_n': 26, 'negative': 0}, {'x_n': 9, 'negative': 0}, {'x_n': 13, 'negative': 0}], [{'x_n': 11, 'negative': 0}, {'x_n': 22, 'negative': 1}, {'x_n': 25, 'negative': 0}], [{'x_n': 14, 'negative': 1}, {'x_n': 21, 'negative': 1}, {'x_n': 17, 'negative': 0}], [{'x_n': 0, 'negative': 1}, {'x_n': 21, 'negative': 0}, {'x_n': 24, 'negative': 0}], [{'x_n': 1, 'negative': 0}, {'x_n': 6, 'negative': 1}, {'x_n': 29, 'negative': 0}], [{'x_n': 21, 'negative': 1}, {'x_n': 20, 'negative': 1}, {'x_n': 24, 'negative': 0}], [{'x_n': 11, 'negative': 0}, {'x_n': 29, 'negative': 0}, {'x_n': 17, 'negative': 1}], [{'x_n': 5, 'negative': 1}, {'x_n': 11, 'negative': 1}, {'x_n': 21, 'negative': 0}], [{'x_n': 9, 'negative': 0}, {'x_n': 11, 'negative': 0}, {'x_n': 6, 'negative': 0}], [{'x_n': 21, 'negative': 0}, {'x_n': 0, 'negative': 0}, {'x_n': 9, 'negative': 0}], [{'x_n': 10, 'negative': 0}, {'x_n': 14, 'negative': 0}, {'x_n': 18, 'negative': 0}], [{'x_n': 1, 'negative': 0}, {'x_n': 19, 'negative': 1}, {'x_n': 4, 'negative': 1}], [{'x_n': 2, 'negative': 0}, {'x_n': 12, 'negative': 1}, {'x_n': 20, 'negative': 0}], [{'x_n': 1, 'negative': 0}, {'x_n': 21, 'negative': 1}, {'x_n': 6, 'negative': 1}], [{'x_n': 25, 'negative': 0}, {'x_n': 3, 'negative': 1}, {'x_n': 13, 'negative': 0}], [{'x_n': 25, 'negative': 1}, {'x_n': 19, 'negative': 1}, {'x_n': 6, 'negative': 1}], [{'x_n': 28, 'negative': 1}, {'x_n': 23, 'negative': 0}, {'x_n': 7, 'negative': 1}], [{'x_n': 8, 'negative': 0}, {'x_n': 18, 'negative': 1}, {'x_n': 0, 'negative': 0}], [{'x_n': 14, 'negative': 0}, {'x_n': 12, 'negative': 1}, {'x_n': 0, 'negative': 1}]], [[{'x_n': 18, 'negative': 1}, {'x_n': 13, 'negative': 0}, {'x_n': 14, 'negative': 0}], [{'x_n': 4, 'negative': 1}, {'x_n': 5, 'negative': 0}, {'x_n': 0, 'negative': 1}], [{'x_n': 19, 'negative': 0}, {'x_n': 20, 'negative': 0}, {'x_n': 28, 'negative': 1}], [{'x_n': 25, 'negative': 1}, {'x_n': 15, 'negative': 1}, {'x_n': 6, 'negative': 0}], [{'x_n': 10, 'negative': 1}, {'x_n': 27, 'negative': 1}, {'x_n': 11, 'negative': 1}], [{'x_n': 20, 'negative': 1}, {'x_n': 8, 'negative': 0}, {'x_n': 22, 'negative': 0}], [{'x_n': 3, 'negative': 0}, {'x_n': 1, 'negative': 1}, {'x_n': 11, 'negative': 0}], [{'x_n': 12, 'negative': 1}, {'x_n': 1, 'negative': 1}, {'x_n': 5, 'negative': 0}], [{'x_n': 25, 'negative': 0}, {'x_n': 4, 'negative': 1}, {'x_n': 27, 'negative': 1}], [{'x_n': 23, 'negative': 0}, {'x_n': 22, 'negative': 1}, {'x_n': 5, 'negative': 1}], [{'x_n': 15, 'negative': 0}, {'x_n': 13, 'negative': 1}, {'x_n': 14, 'negative': 1}], [{'x_n': 13, 'negative': 0}, {'x_n': 10, 'negative': 1}, {'x_n': 12, 'negative': 1}], [{'x_n': 9, 'negative': 0}, {'x_n': 14, 'negative': 1}, {'x_n': 22, 'negative': 0}], [{'x_n': 16, 'negative': 0}, {'x_n': 20, 'negative': 0}, {'x_n': 1, 'negative': 1}], [{'x_n': 11, 'negative': 1}, {'x_n': 1, 'negative': 1}, {'x_n': 7, 'negative': 0}], [{'x_n': 2, 'negative': 1}, {'x_n': 12, 'negative': 1}, {'x_n': 13, 'negative': 1}], [{'x_n': 3, 'negative': 0}, {'x_n': 20, 'negative': 1}, {'x_n': 12, 'negative': 1}], [{'x_n': 11, 'negative': 1}, {'x_n': 0, 'negative': 0}, {'x_n': 16, 'negative': 0}], [{'x_n': 14, 'negative': 0}, {'x_n': 5, 'negative': 0}, {'x_n': 25, 'negative': 1}], [{'x_n': 15, 'negative': 0}, {'x_n': 18, 'negative': 1}, {'x_n': 20, 'negative': 1}], [{'x_n': 2, 'negative': 0}, {'x_n': 19, 'negative': 0}, {'x_n': 21, 'negative': 0}], [{'x_n': 25, 'negative': 0}, {'x_n': 2, 'negative': 1}, {'x_n': 3, 'negative': 0}], [{'x_n': 9, 'negative': 1}, {'x_n': 4, 'negative': 0}, {'x_n': 23, 'negative': 0}], [{'x_n': 26, 'negative': 1}, {'x_n': 0, 'negative': 0}, {'x_n': 23, 'negative': 1}], [{'x_n': 19, 'negative': 1}, {'x_n': 9, 'negative': 1}, {'x_n': 21, 'negative': 0}], [{'x_n': 29, 'negative': 0}, {'x_n': 10, 'negative': 1}, {'x_n': 16, 'negative': 1}], [{'x_n': 0, 'negative': 0}, {'x_n': 23, 'negative': 1}, {'x_n': 28, 'negative': 0}]], [[{'x_n': 24, 'negative': 1}, {'x_n': 23, 'negative': 0}, {'x_n': 6, 'negative': 1}], [{'x_n': 26, 'negative': 0}, {'x_n': 3, 'negative': 1}, {'x_n': 29, 'negative': 1}], [{'x_n': 16, 'negative': 0}, {'x_n': 17, 'negative': 0}, {'x_n': 18, 'negative': 1}], [{'x_n': 3, 'negative': 1}, {'x_n': 16, 'negative': 1}, {'x_n': 9, 'negative': 1}], [{'x_n': 14, 'negative': 0}, {'x_n': 13, 'negative': 0}, {'x_n': 29, 'negative': 0}], [{'x_n': 19, 'negative': 0}, {'x_n': 27, 'negative': 0}, {'x_n': 1, 'negative': 1}], [{'x_n': 12, 'negative': 1}, {'x_n': 22, 'negative': 0}, {'x_n': 17, 'negative': 0}], [{'x_n': 18, 'negative': 0}, {'x_n': 9, 'negative': 0}, {'x_n': 29, 'negative': 1}], [{'x_n': 13, 'negative': 1}, {'x_n': 4, 'negative': 0}, {'x_n': 0, 'negative': 1}], [{'x_n': 20, 'negative': 0}, {'x_n': 14, 'negative': 0}, {'x_n': 29, 'negative': 0}], [{'x_n': 17, 'negative': 0}, {'x_n': 28, 'negative': 0}, {'x_n': 27, 'negative': 0}], [{'x_n': 18, 'negative': 1}, {'x_n': 11, 'negative': 0}, {'x_n': 3, 'negative': 0}], [{'x_n': 11, 'negative': 1}, {'x_n': 25, 'negative': 1}, {'x_n': 24, 'negative': 1}], [{'x_n': 1, 'negative': 0}, {'x_n': 12, 'negative': 0}, {'x_n': 26, 'negative': 0}], [{'x_n': 27, 'negative': 1}, {'x_n': 4, 'negative': 0}, {'x_n': 26, 'negative': 1}], [{'x_n': 23, 'negative': 0}, {'x_n': 29, 'negative': 0}, {'x_n': 25, 'negative': 0}], [{'x_n': 25, 'negative': 0}, {'x_n': 23, 'negative': 1}, {'x_n': 20, 'negative': 0}], [{'x_n': 26, 'negative': 0}, {'x_n': 15, 'negative': 0}, {'x_n': 23, 'negative': 0}], [{'x_n': 17, 'negative': 0}, {'x_n': 25, 'negative': 1}, {'x_n': 2, 'negative': 1}], [{'x_n': 8, 'negative': 1}, {'x_n': 11, 'negative': 1}, {'x_n': 10, 'negative': 0}], [{'x_n': 15, 'negative': 1}, {'x_n': 4, 'negative': 0}, {'x_n': 24, 'negative': 0}], [{'x_n': 19, 'negative': 0}, {'x_n': 20, 'negative': 0}, {'x_n': 15, 'negative': 0}], [{'x_n': 21, 'negative': 0}, {'x_n': 12, 'negative': 0}, {'x_n': 17, 'negative': 0}], [{'x_n': 27, 'negative': 1}, {'x_n': 11, 'negative': 1}, {'x_n': 0, 'negative': 1}], [{'x_n': 16, 'negative': 0}, {'x_n': 10, 'negative': 1}, {'x_n': 24, 'negative': 1}], [{'x_n': 15, 'negative': 1}, {'x_n': 8, 'negative': 0}, {'x_n': 24, 'negative': 0}], [{'x_n': 27, 'negative': 1}, {'x_n': 15, 'negative': 1}, {'x_n': 17, 'negative': 1}]]]

# tworzenie genomu o dlugosci length zlozony z 0 i 1
def generate_genome(length):
    return choices([0, 1], k=length)
# przykładowy genom: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]


# tworzenie populacji genomow o dlugosci genome_length i liczebnosci size
def generate_population(size, genome_length):
    return [generate_genome(genome_length) for _ in range(size)]


# cross genomow w polowie dlugosci, [p:] znaczy od p do końca
def crossover(a, b):
    length = len(a)

    p = int(length / 2)
    return a[0:p] + b[p:], b[0:p] + a[p:]


# mutacja elementu genomu na poziomie probability
def mutation(genome, num=1, probability=0.5):
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome


# wybor par do nastepnej generacji z populacji o wagach weights i bierzemy 2
def selection_pair(population, weights):
    return choices(
        population=population,
        weights=weights,
        k=2
    )



# ewolucja
def run_evolution(
        populate_func,
        fitness_func,
        fitness_limit,
        mutation_func=mutation,
        generation_limit=100):
    global i
    population = populate_func()  # tworzymy populacje
    maks = []
    averag = []
    for i in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome),
                            reverse=True)  # sortujemy wedlug funkcji fitness

        # znaczy ze mamy maksa
        if fitness_func(population[0]) == fitness_limit:
            break
        # jeśli nie to nowa generaca, wybieray dwie najlepsze z populacji
        next_generation = population[0:2]  # elityzm -> dwie najlepsze przechodza dalej
        weights = [fitness_func(gene) for gene in population]  # wagi do wybierania par
        for j in range(int(len(population) / 2) - 1):
            parents = selection_pair(population, weights)  # wybieramy dwie pary do crossowania
            offspring_a, offspring_b = crossover(parents[0], parents[1])  # cross dwoch par
            offspring_a = mutation_func(offspring_a)  # mutacja potomka
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]  # dodanie do nastepnej generacji

        averag.append(sum(weights) / len(weights))  # statystyki
        maks.append(fitness_func(population[0]))
        population = next_generation

    return population, i, maks, averag


def run_bruteforce(
        n_variables,
        fitness_func,
        fitness_limit):
    iteration_list = [0] * n_variables
    maks_value = 0
    i = 1
    # tu odnajduje najlepsza funkcje fitness
    while sum(iteration_list) <= n_variables:
        iter_value = fitness_func(iteration_list)
        # jeśli wszystkie spełniaja
        if iter_value == fitness_limit:
            maks_value = iter_value
            break
        if iter_value > maks_value:
            maks_value = iter_value

        index = int(len(iteration_list) - 1)
        while True:
            iteration_list[index] = iteration_list[index] + 1
            if iteration_list[0] == 2:
                break
            if iteration_list[index] == 2:
                iteration_list[index] = 0
                index = index - 1
            else:
                break
        if iteration_list[0] == 2:
            break
        i += 1
    return maks_value, i, iteration_list

n_variables = 30 #30,15,3 to jest ilosc zmiennych x1,x2,x3,...,xn
n_formulas = 3 #ile bedzie formulas
n_c = 30#27,12,3 tu ile bedzie formul w liscie formulas
formulas = []
formula = []
for i in range(0, n_formulas):
    while len(formula) < n_c:
        x1 = randint(0,n_variables-1)
        x2 = randint(0,n_variables-1)
        x3 = randint(0,n_variables-1)
        if x1 != x2 and x1 != x3 and x2 != x3:
            formula.append([{"x_n": x1, "negative": randint(0,1)}, {"x_n": x2, "negative": randint(0,1)}, {"x_n": x3, "negative": randint(0,1)}])
    formulas.append(formula)
    formula = []
# print(formulas)
# print("3 SAT BRUTEFORCE")
# print("--------")
# start = time.time()
# maks_brute_value, brute_generations, iteration_bruteforce = run_bruteforce(
#     n_variables = n_variables,
#     fitness_func = partial(fitness, formulas=formulas),
#     fitness_limit = n_formulas*n_c) #limit jest taki ile nawiasów ogolnie
# end= time.time()
# print("FINISH")
# print('it took: ', end-start)

# if (brute_generations >= 2**n_variables):
#     print("Nie ma rozwiazania")
#     print('best fitness value', maks_brute_value)
#     print('what genom looks like',iteration_bruteforce)
# else:
#     print("Jest takie rozwiazanie")
#     print('best fitness value', maks_brute_value)
#     print('what genom looks like', iteration_bruteforce)
#     print("Znaleziono w {} iteracji".format(brute_generations))
# print(" ")

print("3 SAT GENETIC ALGORYTM 1")
print("--------")

start2=time.time()
population, generations, maks, averag = run_evolution(
    populate_func=partial(generate_population, size=100, genome_length=n_variables),
    fitness_func=partial(fitness, formulas=formulas),
    fitness_limit=n_formulas*n_c,
    generation_limit=300
)
print(maks,averag)
end2=time.time()

print("FINISH")
print('it took', end2-start2) #tu chyba powinnam osobne patrzec
# bo to znaczy ze wszystkie nawiasy są git
if (fitness(population[0], formulas)) == n_formulas*n_c:
    print("Jest to mozliwe aby znalezc takie zmienne: ")
else:
    print("Nie mozliwe aby znalezc takie zmienne, najlepsze rozwiazanie: ")
print('best fitness value',fitness(population[0], formulas))
print('what genom looks like', population[0])
print('iteracja', generations)

#
# x=[]
# y1=[]
# y2=[]
# y3=[]
#
x = list(range(1, len(maks) + 1))
#
#
# red_patch = mpatches.Patch(color='red', label='maksymalnie')
# blue_patch = mpatches.Patch(color='blue', label='srednia')
# plt.legend(handles=[red_patch, blue_patch])
# plt.plot(x, maks, 'r')
# plt.plot(x, averag, 'b')
# plt.ylabel('Fitness [ocena]')
# plt.xlabel('Pokolenie')
# plt.title('Działanie algorytmu genetycznego dla 3-SAT')
# plt.show()















print('start')
n_variables = 20
n_formulas = 12
n_c = 6
formulas = []
formula = []
for i in range(0, n_formulas):
    while len(formula) < n_c:
        x1 = randint(0, n_variables - 1)
        x2 = randint(0, n_variables - 1)
        x3 = randint(0, n_variables - 1)
        if x1 != x2 and x1 != x3 and x2 != x3:
            formula.append([{"x_n": x1, "negative": randint(0, 1)}, {"x_n": x2, "negative": randint(0, 1)},
                            {"x_n": x3, "negative": randint(0, 1)}])
    formulas.append(formula)
    formula = []

start = time.time()
_, brute_generations, _ = run_bruteforce(
    n_variables=n_variables,
    fitness_func=partial(fitness, formulas=formulas),
    fitness_limit=n_formulas * n_c)
end = time.time()
brute1 = end - start
if (brute_generations >= 2 ** n_variables):
    print("Nie ma rozwiazania 1")

start = time.time()
population, _, _, _ = run_evolution(
    populate_func=partial(generate_population, size=100, genome_length=n_variables),
    fitness_func=partial(fitness, formulas=formulas),
    fitness_limit=n_formulas * n_c,
    generation_limit=300
)
end = time.time()
gene1 = end - start

n_variables2 = 15
formulas = []
formula = []
for i in range(0, n_formulas):
    while len(formula) < n_c:
        x1 = randint(0, n_variables2 - 1)
        x2 = randint(0, n_variables2 - 1)
        x3 = randint(0, n_variables2 - 1)
        if x1 != x2 and x1 != x3 and x2 != x3:
            formula.append([{"x_n": x1, "negative": randint(0, 1)}, {"x_n": x2, "negative": randint(0, 1)},
                            {"x_n": x3, "negative": randint(0, 1)}])
    formulas.append(formula)
    formula = []

start = time.time()
_, brute_generations2, _ = run_bruteforce(
    n_variables=n_variables2,
    fitness_func=partial(fitness, formulas=formulas),
    fitness_limit=n_formulas * n_c)

end = time.time()
brute2 = end - start

if (brute_generations2 >= 2 ** n_variables2):
    print("Nie ma rozwiazania 2")

start = time.time()
population2, _, _, _ = run_evolution(
    populate_func=partial(generate_population, size=100, genome_length=n_variables2),
    fitness_func=partial(fitness, formulas=formulas),
    fitness_limit=n_formulas * n_c,
    generation_limit=300
)

end = time.time()
gene2 = end - start

n_variables3 = 10
formulas = []
formula = []
for i in range(0, n_formulas):
    while len(formula) < n_c:
        x1 = randint(0, n_variables3 - 1)
        x2 = randint(0, n_variables3 - 1)
        x3 = randint(0, n_variables3 - 1)
        if x1 != x2 and x1 != x3 and x2 != x3:
            formula.append([{"x_n": x1, "negative": randint(0, 1)}, {"x_n": x2, "negative": randint(0, 1)},
                            {"x_n": x3, "negative": randint(0, 1)}])
    formulas.append(formula)
    formula = []

start = time.time()
_, brute_generations3, _ = run_bruteforce(
    n_variables=n_variables3,
    fitness_func=partial(fitness, formulas=formulas),
    fitness_limit=n_formulas * n_c)

end = time.time()
brute3 = end - start

if (brute_generations3 >= 2 ** n_variables3):
    print("Nie ma rozwiazania 3")

start = time.time()
population3, _, _, _ = run_evolution(
    populate_func=partial(generate_population, size=100, genome_length=n_variables3),
    fitness_func=partial(fitness, formulas=formulas),
    fitness_limit=n_formulas * n_c,
    generation_limit=300
)

end = time.time()
gene3 = end - start

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.27  # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [gene1, gene2, gene3]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [brute1, brute2, brute3]
rects2 = ax.bar(ind + width, zvals, width, color='g')

ax.set_ylabel('Time [s]')
ax.set_xlabel('Inputs')

ax.set_xticks(ind + width)
ax.set_xticklabels(('20', '15', '10'))
ax.legend((rects1[0], rects2[0]), ('Genetic', ' Brute force'))


def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

plt.show()

print('end')
