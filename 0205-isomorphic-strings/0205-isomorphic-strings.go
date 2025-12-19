func isIsomorphic(s string, t string) bool {
    // forwards describes the map from s -> t
    // backwards describes the map from t -> s

    // All ascii characters can be represented in a single byte
    forwards := make(map[byte]byte)
    backwards := make(map[byte]byte)

    for i := range len(s) {
        schar := s[i]
        tchar := t[i]

        // violation of constraints
        if value, exists := forwards[schar]; exists && value != tchar {
            return false
        }
        if value, exists := backwards[tchar]; exists && value != schar {
            return false
        }

        // assign 
        forwards[schar] = tchar
        backwards[tchar] = schar
    }
    return true
}