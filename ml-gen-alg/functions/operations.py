import numpy as np
import random

def example():
    return "¡Funciona correctamente!"

def objective_funtion(x):
  return x ** 2

def create_individualism(min_value, max_value):
  return random.uniform(min_value, max_value)

def create_population(size, min_value, max_value):
  return [create_individualism(min_value, max_value) for _ in range(size)]

# Selection
def evaluate_population(population):
  return [objective_funtion(x) for x in population]

def tournament_selection(population, rates, key = 3):
  selected_index = random.sample(range(len(population)), key)
  selected_rates = [rates[i] for i in selected_index]
  best_index = selected_rates.index(min(selected_rates))
  return population[selected_index[best_index]]

# Aritmetic cross
def aritmetic_cross(parent1, parent2, cross_rate):
  if random.random() < cross_rate:
    child = (parent1 + parent2)/2
    return child
  return parent1 if random.random() < 0.5 else parent2

# Mutation
def mutation(individual, mutation_rate, min_value, max_value):
  if random.random() < mutation_rate:
    return create_individualism(min_value, max_value)
  return individual

  population = create_population(population_size, min_value, max_value)
def genetic_algorithm(population_size, generations, min_value, max_value, cross_rate, mutation_rate, elitism_rate):
  population = create_population(population_size, min_value, max_value)

  for generation in range(generations):
    rates = evaluate_population(population)

    sorted_population = [x for _, x in sorted(zip(rates, population))]

    next_generation = sorted_population[:int(elitism_rate)]

    while len(next_generation) < population_size:

      # Selection operator
      parent1 = tournament_selection(sorted_population, rates)
      parent2 = tournament_selection(sorted_population, rates)

      # Cross operator
      child = aritmetic_cross(parent1, parent2, cross_rate)

      # Mutation operator
      child = mutation(child, mutation_rate, min_value, max_value)

      next_generation.append(child)

    population = next_generation

    current_rates = evaluate_population(population)
    best_rate = min(current_rates)
    best_index = current_rates.index(best_rate)
    best_individual = population[best_index]

    print(f"Generacion: {generation + 1} - Mejor individuo: {best_individual} - Mejor valor: {best_rate}")
  print(f"MEJOR INDIVIDUO PARA X **2: {best_individual}")
  return best_individual
