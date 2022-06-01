import pygad
import numpy

S = [
    ['Zegar', 100, 7],
    ['Obraz-pejzaż', 300, 7],
    ['Obraz-portret', 200, 6],
    ['Radio', 40, 2],
    ['Laptop', 500, 5],
    ['Lampka nocna', 70, 6],
    ['Srebrne sztućce', 100, 1],
    ['Porcelana', 250, 3],
    ['Figura z brązu', 300, 10],
    ['Skórzana torebka', 280, 3],
    ['Odkurzacz', 300, 15]
]

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcjÄ fitness
def fitness_func(solution, solution_idx):
    weight_limit=25
    if len(solution) != len(S):
        raise ValueError("genome and things must be of same length")

    weight = 0
    value = 0
    for i, thing in enumerate(S):
        if solution[i] == 1:
            weight += thing[2]
            value += thing[1]

            if weight > weight_limit:
                return 0

    return value

fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = len(S)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 60
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 10

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

#uruchomienie algorytmu
ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
# print(S,solution)
# prediction = numpy.sum(S*solution)
# print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
objects=[]
prediction=0
weight=0
for i in range(0,len(S)-1):
    # print(i, solution[i])
    if solution[i]==1.0:
        objects.append(S[i][0])
        prediction+=S[i][1]
        weight+=S[i][2]
print(objects)
print('weight: ', weight)

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()