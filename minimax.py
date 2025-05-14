def minimax(depth, is_maximizing, values, index):
    if depth == 2:
        return values[index]

    if is_maximizing:
        left = minimax(depth + 1, False, values, index * 2)
        right = minimax(depth + 1, False, values, index * 2 + 1)
        return max(left, right)
    else:
        left = minimax(depth + 1, True, values, index * 2)
        right = minimax(depth + 1, True, values, index * 2 + 1)
        return min(left, right)

print("Enter 4 leaf node values (space separated): ")
user_input = input()
values = list(map(int, user_input.strip().split()))

if len(values) != 4:
    print("Error: Please enter exactly 4 values.")
else:
    best_value = minimax(0, True, values, 0)
    print("The best value is:", best_value)
