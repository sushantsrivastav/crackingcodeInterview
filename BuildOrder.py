from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj_list = defaultdict(list)

        for dest, src in prerequisites:
            adj_list[src].append(dest)
        topological_sort_order = []
        is_possible = True

        color = {k: 'white' for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            color[node] = 'gray'

            if node in adj_list:
                for neighbour in adj_list[node]:
                    if color[neighbour] == 'white':
                        dfs(neighbour)
                    elif color[neighbour] == 'gray':
                        is_possible = False
            color[node] = 'black'
            topological_sort_order.append(node)

        for vertex in range(numCourses):
            if color[vertex] == 'white':
                dfs(vertex)
        return topological_sort_order[::-1] if is_possible else []




