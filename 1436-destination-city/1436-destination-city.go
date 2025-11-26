func destCity(paths [][]string) string {
    // A destination city will have no out degree in a graph sense
    // so we would need to note that it would be a value but not a key in our hashmap   

    destinations := make(map[string]string, len(paths))
    // populate hashmap from start -> end
    for _, dest := range paths {
        start, end := dest[0], dest[1]
        destinations[start] = end
    }

    // loop over all ends and make sure it does not exist as a start
    for _, end := range destinations {
        if _, exists := destinations[end]; !exists {
            return end
        }
    }
    // Guarenteed to exist
    return ""
}