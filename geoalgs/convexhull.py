
# Returns true if points A->B->C form a clockwise-convex chain.
# Takes care of duplicate and nearly identical points.
def points_make_a_right_turn(A,B,C):
    ABx = B.x() - A.x()
    ABy = B.y() - A.y()
    BCx = C.x() - B.x()
    BCy = C.y() - B.y()
    return BCx*ABy-BCy*ABx > 0

def remove_second_last(points):
    assert len(points) > 1
    del points[-2] 

def compute_half_hull(points):
    half_hull = points[:2]
    for point in points[2:]:
        half_hull.append(point)
        while len(half_hull) > 2 and not points_make_a_right_turn(*half_hull[-3:]):
            remove_second_last(half_hull)
    return half_hull

def convex_hull_2D(input_points):
    sorted_points = sorted(input_points)
    if len(sorted_points) < 3:
        return sorted_points

    upper_hull = compute_half_hull(sorted_points)
    lower_hull = compute_half_hull(sorted_points[::-1])
    
    return upper_hull + lower_hull[1:-1]