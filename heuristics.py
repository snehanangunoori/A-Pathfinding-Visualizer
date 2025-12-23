def manhattan_distance(node, goal):
    x_dist = abs(node.row - goal.row)
    y_dist = abs(node.col - goal.col)
    
    return x_dist + y_dist

# Additional heuristic function for potential future use
def euclidean_distance(node, goal):
    x_dist = node.row - goal.row
    y_dist = node.col - goal.col
    
    x_dist_sq = x_dist * x_dist
    y_dist_sq = y_dist * y_dist
    
    return (x_dist_sq + y_dist_sq) ** 0.5