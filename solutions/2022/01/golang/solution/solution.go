package solution

import (
	"fmt"
	"log"
	"sort"
	"strconv"
	"strings"

	"github.com/frek818/aocdata"
)

func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func parseCalories(elf_data string) []int {
	var calories []int
	for _, line := range strings.Split(elf_data, "\n") {
		if line == "" {
			continue
		}
		intVar, err := strconv.Atoi(line)
		if err != nil {
			log.Fatal(err)
		}
		calories = append(calories, intVar)
	}
	return calories
}

func parseElvesCalories(input_data string) [][]int {
	elves_data := strings.Split(input_data, "\n\n")
	var elves_calories [][]int
	for _, elf_data := range elves_data {
		elf_calories := parseCalories(elf_data)
		elves_calories = append(elves_calories, elf_calories)
	}
	return elves_calories
}

func sortedSumElvesCalories(elves_calories [][]int, reverse bool) []int {
	var elves_calorie_sum []int
	for _, elf_calories := range elves_calories {
		elves_calorie_sum = append(elves_calorie_sum, sum(elf_calories))
	}

	sort.Ints(elves_calorie_sum)

	if reverse {
		sort.Sort(sort.Reverse(sort.IntSlice(elves_calorie_sum)))
	}

	return elves_calorie_sum
}

func Solution1(input_data string) int {
	elves_calories := parseElvesCalories(input_data)
	elves_calorie_sum := sortedSumElvesCalories(elves_calories, true)
	return elves_calorie_sum[0]
}

func Solution2(input_data string) int {
	elves_calories := parseElvesCalories(input_data)
	elves_calorie_sum := sortedSumElvesCalories(elves_calories, true)
	return sum(elves_calorie_sum[0:3])
}

func Runner() {
	input_data := aocdata.GetInputData(2022, 1)
	fmt.Printf("Solution 1 = %v\n", Solution1(input_data))
	fmt.Printf("Solution 2 = %v\n", Solution2(input_data))
}
