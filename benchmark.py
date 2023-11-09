import timeit
from main import solution


def benchmark_solution():
    # Executar a função solution() várias vezes e calcular o tempo médio
    setup_code = '''
from __main__ import solution
s = "abacabad"
    '''
    run_code = '''
solution(s)
    '''

    # Define o número de iterações e repete a execução
    iterations = 100000
    time_taken = timeit.timeit(run_code, setup=setup_code, number=iterations)

    # Calcula o tempo médio por iteração
    avg_time_per_iteration = time_taken / iterations

    print(f'Tempo médio por iteração: {avg_time_per_iteration:.6f} segundos')


# Executa o benchmark
benchmark_solution()
