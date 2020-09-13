from collections import deque  # deque для комфортной работы с очередью
N, M = map(int, input().split(' '))  # Считываем размер поля
graph = {i: set() for i in range(N*M)}  # Задаем N ключей для словаря
k = 0
bombs = 1

distances = [None] * N * M  # Массив под расстояния
start_vertex = 0  # Стартовая точка
# Заполнение лабиринта
def make_labirint(N,M,distances):
    distances[start_vertex] = 0
    for i in range(N-2):  # Правая стенка
        distances[M*(i+1)-1] = -1
    for i in range(1, N):  # Левая стенка
        distances[M*i] = -1
    for i in range(M-2):  # далее сверху вниз горизонтальные стенки
        distances[M+i] = -1
    for i in range(M-1):
        distances[M*(N-1)+i] = -1
    for i in range(2, M-1):
        distances[3*M+i] = -1
    for i in range(2, M-1):
        distances[4*M+i] = -1
    for i in range(2, M-2):
        distances[6*M+i] = -1
    for i in range(1, M-2):
        distances[7*M+i] = -1
    distances[8*M+2] = -1
    distances[9*M+2] = -1
    for i in range(4, M-1):
        distances[9*M+i] = -1
    distances[10*M+2] = -1
    for i in range(2, M-2):
        distances[11*M+i] = -1
    distances[12*M+2] = -1
    # 13 пустая
    for i in range(2, M-2):
        distances[14*M+i] = -1
    # 15 пустая
    for i in range(2, M-1):
        distances[16*M+i] = -1
    for i in range(2, M-1):
        distances[17*M+i] = -1
    # Конец заполнения лабиринта

make_labirint(N,M,distances)

def print_green(value):
    print("\033[32m {}".format(distances[i]), end='\t')

def print_red(value):
    print("\033[31m {}".format(distances[i]), end='\t')

def make_edges(distances, graph, N, M):
    for i in range(N): # Построение ребер между вершинами,не явл. стеной, и не выходя за границу поля
        for j in range(M):
            if distances[M*i+j] != -1:
                if j + 1 < M and distances[i*M+j+1] != -1:
                    graph[i*M+j].add(i*M+j+1)
                    graph[i*M+j+1].add(i*M+j)
                if i + 1 < N and distances[M*(i+1)+j] != -1:
                    graph[M*i+j].add(M*(i+1)+j)
                    graph[M*(i+1)+j].add(M*i+j)

make_edges(distances, graph, N, M)
print(graph)

queue = deque([start_vertex])  # Первый эл-т в очередь
parents = [None] * N * M  # Массив предков для восстановления кратчайшего пути

while queue:
    cur_v = queue.popleft()  # Удаляем предка из очереди и записываем в cur_v
    for neigh_v in graph[cur_v]:  # Перебираем эл-ты множеств у соотв. ключей
        if distances[neigh_v] is None or distances[neigh_v] == -1:  # Если мы еще не трогали вершину, то...
            distances[neigh_v] = distances[cur_v] + 1  # Увеличиваем расстояние на 1
            parents[neigh_v] = cur_v  # Записываем предка
            queue.append(neigh_v)  # Добавляем в очередь

for i in range(M*N):
    if i % M == 0:
        print('\n')
    if distances[i] != -1:
        print_green(distances[i])
    else:
        print_red(distances[i])
print('\n\n')


end_vertex = N * M - 1  # Конечная точка
path = [end_vertex]  # Массив пути
parent = parents[end_vertex]
while not parent is None:  # В цикле спускаемся по предкам до стартовой позиции
    path.append(parent)
    parent = parents[parent]
# Для корректного отображения пути path нужно вывести в обратном порядке
path.reverse()

print("\033[34m {}" .format('\n\n Кратчайшее расстояние : '), end=' ')
print(distances[end_vertex])
print('\n Восстановленный путь:', path)
