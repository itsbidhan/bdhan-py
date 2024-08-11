from collections import deque

print("This program uses Breadth-First Search (BFS) to find the path in a tree structure.")

def bfs_path(graph, start, goal):
    # Initialize the queue with the start node and its path
    queue = deque([(start, [start])])
    
    # Set to track visited nodes
    visited = set([start])
    
    while queue:
        current_node, path = queue.popleft()
        
        # Check if we reached the goal
        if current_node == goal:
            return path
        
        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
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
    graph = get_user_input()
    
    start_node = input("\nEnter the start node: ").strip()
    goal_node = input("Enter the goal node: ").strip()
    
    path = bfs_path(graph, start_node, goal_node)
    
    
    if path:
        print("\nPath to goal node:", " -> ".join(path))
    
    else:
        print("No path found to the goal node.")

if __name__ == "__main__":
    main()
