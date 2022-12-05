package main;

import (
	"fmt"
)

func value(a string) int {
	return int(a[0] - 'A') + 1
}

func xvalue(b string) int {
	return int(b[0] - 'X') + 1
}

func beaten(a int, b int) bool {
	return b == a + 1 || (b == 1 && a == 3)
}

func main() {
	ans1, ans2 := 0, 0

	for {
		var as string
		var bs string
		if k, _ := fmt.Scanf("%s %s\n", &as, &bs); k != 2 {
			break
		}

		a := value(as)
		for _, b := range []int{1, 2, 3} {
			score := b
			outcome := "X"
			if beaten(a, b) {
				score += 6
				outcome = "Z"
			} else if (a == b) {
				score += 3
				outcome = "Y"
			}

			if b == xvalue(bs) {
				ans1 += score
			}
			if outcome == bs {
				ans2 += score
			}
		}
	}

	fmt.Println(ans1, ans2)
}
