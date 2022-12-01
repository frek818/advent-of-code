package solution

import (
	"testing"
)

func TestAbs(t *testing.T) {
	got := Solution1()
	if got != 1 {
		t.Errorf("Solution1(input_data) = %d; want ", got)
	}
}
