def print_towers(towers):
    print("\nCurrent state of the towers:")
    for peg in towers:
        print(f"{peg}: {' '.join(map(str, towers[peg]))}")

def move_disk(towers, from_peg, to_peg):
    if not towers[from_peg]:
        print(f"Cannot move from {from_peg}. It's empty.")
        return False
    
    if towers[to_peg] and towers[to_peg][-1] <     towers[from_peg][-1]:
        print(f"Cannot move disk {towers[from_peg][-1]} to {to_peg}. It is larger than the top disk on {to_peg}.")
        return False
    
    towers[to_peg].append(towers[from_peg].pop())
    return True

def towers_of_hanoi_game(n):
    towers = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    print("Welcome to the Towers of Hanoi game!")
    print("Your goal is to move all disks from peg A to peg C using peg B as auxiliary.")
    
    total_moves = 0
    
    while len(towers['C']) != n:
        print_towers(towers)
        
        from_peg = input("Move disk from peg (A, B, C): ").strip().upper()
        to_peg = input("Move disk to peg (A, B, C): ").strip().upper()
        
        if from_peg in towers and to_peg in towers and from_peg != to_peg:
            if move_disk(towers, from_peg, to_peg):
                total_moves += 1
                print(f"Moved disk from {from_peg} to {to_peg}.")
            else:
                print("Invalid move. Please try again.")
        else:
            print("Invalid pegs. Please use 'A', 'B', or 'C' and ensure the source and destination pegs are different.")
    
    print_towers(towers)
    print(f"Congratulations! You've solved the puzzle in {total_moves} moves.")

n = int(input("Enter the number of disks: "))
towers_of_hanoi_game(n)
