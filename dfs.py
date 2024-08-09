"""
Program to implement Depth First Search (DFS) with user input for starting and ending nodes
"""

# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

visited = set()  # Set to keep track of visited nodes of the graph.
found = False  # Variable to indicate when the end node is found.


def dfs(visited, graph, node, end_node):  # function for DFS
    global found
    if node not in visited and not found:
        # Print the node followed by an arrow, except after the last node
        end_char = '->' if node != end_node else ''
        print(node, end=end_char)
        visited.add(node)
        if node == end_node:
            found = True
            return
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, end_node)


# Driver Code
start_node = input("Enter the starting node: ").upper()
end_node = input("Enter the ending node: ").upper()

if start_node in graph and end_node in graph:
    print("Following is the Depth-First Search")
    dfs(visited, graph, start_node, end_node)
else:
    print("One or both of the entered nodes are not present in the graph.")
