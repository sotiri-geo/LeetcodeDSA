// isPathCrossing returns true if there exists a point which has previously 
// been visited whilst traversing path, else return false.
func isPathCrossing(path string) bool {
    type Point struct{
        X int
        Y int
    }
    // Preallocate to avoid realloc
    visited := make(map[Point]struct{}, len(path) + 1)
    curr := Point{0, 0}
    visited[curr] = struct{}{}

    for _, direction := range path {
        switch direction {
            case 'N':
                curr.Y++
            case 'S': 
                curr.Y--
            case 'E':
                curr.X++
            case 'W':
                curr.X--
        }
        
        // check if we overlapped
        if _, hasCrossed := visited[curr]; hasCrossed {
            return true
        }

        visited[curr] = struct{}{}
    }
    return false
}