package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	buf, err := io.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}
	text := string(buf)

	sums := []int{}
	for _, block := range strings.Split(text, "\n\n") {
		block = strings.Trim(block, "\n")

		sum := 0
		for _, token := range strings.Split(block, "\n") {
			if val, err := strconv.Atoi(token); err != nil {
				panic(err)
			} else {
				sum += val
			}
		}
		sums = append(sums, sum)
	}

	sort.Sort(sort.Reverse(sort.IntSlice(sums)))
	fmt.Printf("%d\n%d\n", sums[0], sums[0]+sums[1]+sums[2])
}
