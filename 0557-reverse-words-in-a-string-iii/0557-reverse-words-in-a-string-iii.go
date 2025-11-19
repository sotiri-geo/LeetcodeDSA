import "strings"

func reverse(s string) string {
    var ans strings.Builder

    for i := len(s) - 1; i >= 0; i-- {
        ans.WriteByte(s[i])
    }
    return ans.String()
}

func reverseWords(s string) string {
    var ans strings.Builder

    words := strings.Fields(s)
    ans.Grow(len(s)) // Avoids realloc 

    for i, word := range words {
        // Add a space before each word instead of the first
        if i > 0 {
            ans.WriteByte(' ')
        }

        // In place swapping is more memory efficient than building a new String    
        // Using two pointers to reverese the strings
        runes := []rune(word)   
        for left, right := 0, len(runes) - 1; left < right; left, right = left + 1, right - 1 {
            runes[left], runes[right] = runes[right], runes[left]
        }
        ans.WriteString(string(runes))
    }    

    return ans.String()
}