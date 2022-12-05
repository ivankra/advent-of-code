package main

import (
	"fmt"
	"sort"
)

func main() {
	sums := []int{}
	for {
		sum, cnt := 0, 0
		for {
			var x int
			if k, _ := fmt.Scanln(&x); k == 0 {
				break
			}
			sum += x
			cnt += 1
		}
		if cnt == 0 {
			break
		}
		sums = append(sums, sum)
	}

	sort.Sort(sort.Reverse(sort.IntSlice(sums)))
	fmt.Printf("%d\n%d\n", sums[0], sums[0]+sums[1]+sums[2])
}
