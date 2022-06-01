import pygad
import math

# 0 to ściana, 1 to droga
maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

START_LOCATION = [1,1]
END_LOCATION = [10,10]
gene_space = [1,2,3,4]
# [up,down,right,left]

# cofaj jedno jeszcze
def fitness_func(individual,solution_idx):
    currLoc = [1, 1]
    lastMove = None

    for move in individual:

        # UP
        if move == 1 and maze[currLoc[0] - 1][currLoc[1]] == 1 and lastMove != 2:
                currLoc = [currLoc[0] - 1, currLoc[1]]
                lastMove = 1

        # DOWN
        elif move == 2 and maze[currLoc[0] + 1][currLoc[1]] == 1 and lastMove != 1:
                currLoc = [currLoc[0] + 1, currLoc[1]]
                lastMove = 2

        # RIGHT
        elif move == 3 and maze[currLoc[0]][currLoc[1] + 1] == 1 and lastMove != 4:
                currLoc = [currLoc[0], currLoc[1] + 1]
                lastMove = 3

        # LEFT
        elif move == 4 and maze[currLoc[0]][currLoc[1] - 1] == 1 and lastMove != 3:
                currLoc = [currLoc[0], currLoc[1] - 1]
                lastMove = 4
        else:
            continue

    # CALCULATE EUCLIDEAN DISTANCE
    x = currLoc[0] - END_LOCATION[0]
    y = currLoc[1] - END_LOCATION[1]

    distance = -x-y

    # CALCULATE VALUE
    value = -(distance)
    # print(value)
    return value

def chromosomeToData(chromosome):
    moves = []
    movesCount = 0
    currLoc = [1, 1]
    found = False
    lastMove=None
    global result

    for i in chromosome:

        # UP
        if i == 1 and maze[currLoc[0] - 1][currLoc[1]] == 1 and lastMove != 2:
            lastMove = 1
            moves.append("UP")
            currLoc = [currLoc[0] - 1, currLoc[1]]
            movesCount += 1

        # DOWN
        elif i == 2 and maze[currLoc[0] + 1][currLoc[1]] == 1 and lastMove != 1:
            moves.append("DOWN")
            currLoc = [currLoc[0] + 1, currLoc[1]]
            movesCount += 1
            lastMove = 2

        # RIGHT
        elif i == 3 and maze[currLoc[0]][currLoc[1] + 1] == 1 and lastMove != 4:
            moves.append("RIGHT")
            currLoc = [currLoc[0], currLoc[1] + 1]
            movesCount += 1
            lastMove = 3

        # LEFT
        elif i == 4 and maze[currLoc[0]][currLoc[1] - 1] == 1 and lastMove != 3:
            moves.append("LEFT")
            currLoc = [currLoc[0], currLoc[1] - 1]
            movesCount += 1
            lastMove = 4
        else:
            continue


    if currLoc == [10, 10]:
        found = True

    return [moves, movesCount, found]


fitness_function = fitness_func


sol_per_pop = 10
num_genes = 30

num_parents_mating = 5
num_generations = 200
keep_parents = 2

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10

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
result=chromosomeToData(solution)
print("Moves: ", result[0])
print("Moves count: ", result[1])
print("Did found the end: ", result[2])