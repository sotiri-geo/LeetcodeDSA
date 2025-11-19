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

    for i, subString := range words {
        ans.WriteString(reverse(subString))
        if i == len(words) - 1 {
            break
        }
        ans.WriteString(" ")
    }
    
    return ans.String()
}