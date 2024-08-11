def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    
    # Append the start node to the path
    path = path + [start]
    
    # Check if we have reached the goal
    if start == goal:
        return path
    
    # Explore neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in path:   
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:  
                return new_path
    
    return None  

def get_user_input():
    graph = {}
    
    print("\nEnter the tree structure (type 'done' when finished):")
    
    while True:
        node = input("Enter node (or 'done' to finish): ").strip()
        if node.lower() == 'done':
            break
        
        children = input(f"Enter children of node '{node}' (space-separated): ").strip()
        graph[node] = children.split() if children else []
    
    return graph

def main():
    print("This program uses Depth-First Search (DFS) to find the path in a tree structure.")
    
    graph = get_user_input()
    
    start_node = input("\nEnter the start node: ").strip()
    goal_node = input("Enter the goal node: ").strip()
    
    path = dfs_path(graph, start_node, goal_node)
    
    if path:
        print("\nPath to goal node:", " -> ".join(path))
    else:
        print("No path found to the goal node.")

if __name__ == "__main__":
    main()
