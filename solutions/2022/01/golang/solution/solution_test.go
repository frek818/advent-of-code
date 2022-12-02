package solution_test

import (
	"testing"

	"iamjust.dev/aoc/2022/01/solution"
)

func TestSolution1(t *testing.T) {
	input_data := `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
`
	got := solution.Solution1(input_data)
	expected := 24000
	if got != expected {
		t.Errorf("Solution1(`%v`) = %d; want %d", input_data, got, expected)
	}
}

func TestSolution2(t *testing.T) {
	input_data := `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
`
	got := solution.Solution2(input_data)
	expected := 45000
	if got != expected {
		t.Errorf("Solution1(`%v`) = %d; want %d", input_data, got, expected)
	}
}
