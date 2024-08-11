from heapq import heappop, heappush

print("\nThis program uses A* Search (Informed Search) to find the shortest path in a graph.\n")
# In A* Search:
# g(n) = Cost to reach node n from the start node
# h(n) = Heuristic estimate of the cost from node n to the goal node
# f(n) = Total estimated cost of the cheapest solution through node n (f(n) = g(n) + h(n))

def a_star_search(graph, heuristics, start, goal):
# Priority queue to explore nodes based on f(n) = g(n)+h(n)
    open_list = []
    heappush(open_list, (heuristics[start], start))
    
    # Cost to reach each node from start
    g_cost = {start: 0}
    # Total cost function f(n) = g(n) + h(n)
    f_cost = {start: heuristics[start]}
    
    came_from = {start: None}
    closed_list = set()
    
    print(f"Start Node: {start}")
    print(f"Goal Node: {goal}")
    
    while open_list:
        # Get the node with the lowest f(n) value
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
        for neighbor, cost in graph.get(current_node, []):
            tentative_g_cost = g_cost[current_node] + cost
            
           
            if neighbor in closed_list:
                continue
            
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = g_cost[neighbor] + heuristics.get(neighbor, float('inf'))
                came_from[neighbor] = current_node
                
                if neighbor not in [n for _, n in open_list]:
                    print(f"  Adding Neighbor to Open List: {neighbor} (g(n): {g_cost[neighbor]}, h(n): {heuristics.get(neighbor, float('inf'))}, f(n): {f_cost[neighbor]})")
                    heappush(open_list, (f_cost[neighbor], neighbor))
        
        print(f"Open List: {open_list}")
        print(f"Closed List: {closed_list}")
        print("-" * 40)
    
    print("No path found to the goal node.")
    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('H', 2)],
    'G': [('H', 3)],
    'H': []
}

heuristics = {
    'A': 7,'B': 6,
    'C': 5,'D': 4,
    'E': 3,'F': 2,
    'G': 1,'H': 0
}

print("\n")
start_node = 'A'
goal_node = 'G'
print("\n")

a_star_search(graph, heuristics, start_node, goal_node)

