import hatchery.genetic_algorithms as gea
import hatchery.swarm_algorithms as sa
import time

def main():
	inf = float('inf')

	ciudades0 = [[0, 10, 5],
				 [2, 0, 7],
				 [10, 3, 0]]

	ciudades1 = [[0, 8, 9, 1],
				 [1, 0, 6, 4],
				 [15, 1, 0, 8],
				 [6, 3, 16, 0]]

	ciudades2 = [[0, 2, inf, inf, inf],
				 [1, 0, 6, 4, 5],
				 [15, 7, 0, 8, 2],
				 [6, 3, 12, 0, 9],
				 [15, 7, inf, 8, 0]]

	ciudades3 = [[inf, 2, inf, 5],
				 [1, inf, 3, inf],
				 [inf, 2, 10, inf],
				 [5, 6, 1, inf]]

	ciudades4 = [[0, 2, inf, inf, inf, 1, 4],
				 [inf, 0, 6, 4, 5, 19, inf],
				 [inf, 7, 0, 1, 2, 8, 2],
				 [inf, 3, 12, 0, 9, 20, 10],
				 [inf, 7, inf, 8, 0, 1, 3],
				 [inf, 5, 2, inf, 1, 0, 7],
				 [6, 6, inf, inf, inf, 9, 0],]

	start_city = 0

	aco_t1 = time.time()
	aco = sa.ACO(cities = ciudades2, start_city = start_city)
	aco_solution, aco_cost = aco.solve()
	aco_t2 = time.time()

	ga_t1 = time.time()
	ga = gea.GeneticAlgorithm(cities = ciudades2, start_city = start_city)
	ga_solution, ga_cost = ga.solve()
	ga_t2 = time.time()
	
	print("Soluciones de cada algoritmo:")
	print(f"\n* Algoritmo de la colonia de hormigas (ACO)\n\tPunto de inicio: {start_city}\n\tSolucion: {aco_solution}\n\tCosto: {aco_cost}\n\tTiempo: {aco_t1 - aco_t2}")
	print(f"\n* Algoritmos genéticos\n\tPunto de inicio: {start_city}\n\tSolucion: {ga_solution}\n\tCosto: {ga_cost}\n\tTiempo: {ga_t1 - ga_t2}\n")


if __name__ == '__main__':
	main()