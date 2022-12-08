package main

import (
	"bufio"
	"fmt"
	"os"
)

func score(A []string, i, j int) (edge int, scenic int) {
	edge = 0
	scenic = 1

	for _, d := range [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
		vis := 0
		for k := 1; ; k++ {
			ii := i + d[0]*k
			jj := j + d[1]*k
			if !(0 <= ii && ii < len(A) && 0 <= jj && jj < len(A[i])) {
				edge = 1
				break
			}
			vis++
			h := A[i+d[0]*k][j+d[1]*k]
			if h >= A[i][j] {
				break
			}
		}
		scenic *= vis
	}

	return
}

func main() {
	A := []string{}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		A = append(A, line)
	}

	ans1, ans2 := 0, 0
	for i, _ := range A {
		for j, _ := range A[i] {
			edge, scenic := score(A, i, j)
			ans1 += edge
			if scenic > ans2 {
				ans2 = scenic
			}
		}
	}

	fmt.Println(ans1, ans2)
}
