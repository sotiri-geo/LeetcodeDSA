func isPathCrossing(path string) bool {
    // We need to create coorinates to manage 
    type Point struct{
        X int
        Y int
    }
    // Preallocate to avoid realloc
    visited := make(map[Point]struct{}, len(path))
    // initialise
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