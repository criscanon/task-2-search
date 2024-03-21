from search_algorithms.linear_search import linear_search
from search_algorithms.binary_search import binary_search
from search_algorithms.ternary_search import ternary_search
from metrics.measure_time import measure_time
from data_generator.generate_data import generate_data
from graphs.graph import create_graph
import pandas as pd

def main():
    array_size = [100, 500, 2000, 5000, 10000, 20000, 40000, 60000, 80000, 100000]
    target_element = [0, 1, 2, 100]
    results = []
    
    for target in target_element:
        for array in array_size:
            
            # Generate and sort data
            data_array = generate_data(array)
            data_array.sort()

            iteration = []
            iteration.append(target)
            iteration.append(array)
            
            # Linear Search
            result_linear, time_linear = measure_time(linear_search, data_array, target)
            #print(f"Linear Search Result: {result_linear}, Time: {time_linear:.2f} microseconds")
            iteration.append(time_linear)

            # Binary Search
            result_binary, time_binary = measure_time(binary_search, data_array, target)
            #print(f"Binary Search Result: {result_binary}, Time: {time_binary:.2f} microseconds")
            iteration.append(time_binary)

            # Ternary Search
            result_ternary, time_ternary = measure_time(ternary_search, data_array, target)
            #print(f"Ternary Search Result: {result_ternary}, Time: {time_ternary:.2f} microseconds")
            iteration.append(time_ternary)
            results.append(iteration)

    df = pd.DataFrame(results)
    print(df)
    create_graph(results=results, graphs=len(target_element), target_element=target_element)

if __name__ == '__main__':
    main()