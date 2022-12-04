package solution_test

import (
	"testing"

	"iamjust.dev/aoc/2022/01/solution"
)

inputData := `1000
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

func TestSolution1(t *testing.T) {
	got := solution.Solution1(inputData)
	expected := 2
	if got != expected {
		t.Errorf("Solution1(`%v`) = %d; want %d", inputData, got, expected)
	}
}

func TestSolution2(t *testing.T) {
	got := solution.Solution2(inputData)
	expected := 2
	if got != expected {
		t.Errorf("Solution1(`%v`) = %d; want %d", inputData, got, expected)
	}
}
