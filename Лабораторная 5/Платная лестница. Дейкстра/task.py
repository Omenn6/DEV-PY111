from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    start_node = 0
    end_node = max(graph.nodes)

    return nx.dijkstra_path_length(graph, source=start_node, target=end_node, weight="weight")  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)

    stairway_graph = nx.DiGraph()

    n = len(stairway)

    for i in range(n):
        cost = stairway[i - 1] if i > 0 else 0

        stairway_graph.add_edge(i, i + 1, weight=cost)

        if i + 2 <= n:
            stairway_graph.add_edge(i, i + 2, weight=cost)  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    stairway_graph.add_edge(n, n + 1, weight=stairway[-1])

    print(stairway_path(stairway_graph))  # 72
