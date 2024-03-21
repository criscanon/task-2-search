from search_algorithms.linear_search import linear_search
from search_algorithms.binary_search import binary_search
from search_algorithms.ternary_search import ternary_search
from metrics.measure_time import measure_time
from data_generator.generate_data import generate_data

def main():
    array_size = 1000000
    target_element = 0

    # Generate and sort data
    data_array = generate_data(array_size)
    data_array.sort()

    # Linear Search
    result_linear, time_linear = measure_time(linear_search, data_array, target_element)
    print(f"Linear Search Result: {result_linear}, Time: {time_linear:.2f} microseconds")

    # Binary Search
    result_binary, time_binary = measure_time(binary_search, data_array, target_element)
    print(f"Binary Search Result: {result_binary}, Time: {time_binary:.2f} microseconds")

    # Ternary Search
    result_ternary, time_ternary = measure_time(ternary_search, data_array, target_element)
    print(f"Ternary Search Result: {result_ternary}, Time: {time_ternary:.2f} microseconds")

if __name__ == '__main__':
    main()

## Generar combinaciones con diferentes target element y diferentes tamaños de array. (Variar en tamaños de mil en mil, capturar tiempos, generar tabla de cuatro columnas, tiempos.)
## Promediar los tiempos para tener un dato más representativo.