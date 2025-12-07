import (
	"cmp"
	"slices"
	"strings"
)
func frequencySort(s string) string {
    // first need to implement a counter based off hashmap
    count := make(map[rune]int, len(s))

    for _, char := range s {
        count[char]++
    }
    // Create a slice of items for sorting
    type pair struct {
        char rune
        count int
    }

    // Prealloc space
    pairs := make([]pair, 0, len(count))

    // append pairs to array
    for char, freq := range count {
        pairs = append(pairs, pair{char, freq})
    }

    // Desc
    slices.SortFunc(pairs, func(left, right pair) int {
        return cmp.Compare(right.count, left.count)
    })

    // Reconstruct ans
    var ans strings.Builder

    for _, pair := range pairs {
        for range pair.count {
            ans.WriteRune(pair.char)
        }
    }

    return ans.String()
}