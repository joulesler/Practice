package main

import (
	"crypto/sha256"
	"encoding/binary"
	"fmt"
)

func main() {
	groupAnagrams([]string{
		"duh",
		"ill"})
}

func groupAnagrams(strs []string) (retStr [][]string) {
	// Map (hash values -> [index] )

	idxMap := make(map[int][]string)
	for i := 0; i < len(strs); i++ {
		hash := 0
		h := sha256.New()
		for j := 0; j < len(strs[i]); j++ {
			bytesHash := h.Sum([]byte{strs[i][j]})

			hash += int(binary.BigEndian.Uint32(bytesHash[:]))
			fmt.Println(hash, strs[i])

		}
		fmt.Println(hash, strs[i])
		idxMap[hash] = append(idxMap[hash], strs[i])
	}
	for _, value := range idxMap {
		retStr = append(retStr, value)
	}
	return retStr
}
