package main

func isAnagram(s string, t string) bool {
	scharset := make(map[byte]int)
	tcharset := make(map[byte]int)

	if len(s) != len(t) {
		return false
	}

	for char := 0; char < len(s); char++ {
		scharset[s[char]] += 1
		tcharset[t[char]] += 1
	}

	for char := 0; char < len(s); char++ {
		if scharset[s[char]] != tcharset[s[char]] {
			return false
		}
	}
	return true
}
