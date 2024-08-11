from heapq import heappop, heappush

print("\n\nThis program uses Best-First Search (Informed Search) to find the path in a graph.\n")

def best_first_search(graph, heuristics, start, goal):
    open_list = []
    heappush(open_list, (heuristics[start], start))
   
    came_from = {start: None}
    closed_list = set()
    
    print(f"Start Node: {start}")
    print(f"Goal Node: {goal}")
    
    while open_list:
        # Get the node with the lowest heuristic value
        _, current_node = heappop(open_list)
        print(f"Exploring Node: {current_node}")
        
        # Check if the current node is the goal
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()  
            print("\nPath found:", " -> ".join(path))
            return path
        
        closed_list.add(current_node)
        
        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in closed_list and neighbor not in [n for _, n in open_list]:
                print(f"  Adding Neighbor to Open List: {neighbor} (Heuristic: {heuristics.get(neighbor, float('inf'))})")
                came_from[neighbor] = current_node
                heappush(open_list, (heuristics.get(neighbor, float('inf')), neighbor))
        
        print(f"Open List: {open_list}")
        print(f"Closed List: {closed_list}")
        print("-" * 30)
    
    print("No path found to the goal node.")
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

heuristics = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 3,
    'E': 0
}

# Start and goal nodes
start_node = 'A'
goal_node = 'D'

# Run Best-First Search
best_first_search(graph, heuristics, start_node, goal_node)

