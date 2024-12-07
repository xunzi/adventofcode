package main

import (
	"bufio"
	"os"
	"slices"
	"strconv"
	"strings"
)

type sortedSlices struct {
	l1 []int
	l2 []int
}

func ingestDestinationFile(inFile string) ([]string, error) {
	fileHandle, err := os.Open(inFile)
	if err != nil {
		return nil, err
	}
	fileScanner := bufio.NewScanner(fileHandle)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string
	for fileScanner.Scan() {
		//fmt.Println(fileScanner.Text())
		fileLines = append(fileLines, fileScanner.Text())
	}
	fileHandle.Close()
	return fileLines, nil
}

func covertToSortedSlices(inSlice []string) sortedSlices {
	var sl1 []int
	var sl2 []int
	//var sSlice sortedSlices
	for _, line := range inSlice {
		fields := strings.Fields(line)
		f1, _ := strconv.Atoi(fields[0])
		f2, _ := strconv.Atoi(fields[1])
		sl1 = append(sl1, f1)
		sl2 = append(sl2, f2)
	}
	slices.Sort(sl1)
	slices.Sort(sl2)
	return sortedSlices{
		l1: sl1,
		l2: sl2,
	}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func (sSlice sortedSlices) Distances() int {
	var diffs int
	for i, v1 := range sSlice.l1 {
		diffs += abs(v1 - sSlice.l2[i])
	}
	return diffs
}

func (sSlice sortedSlices) Similarity() int {
	var similarity int
	for _, v1 := range sSlice.l1 {
		c := 0
		for _, v2 := range sSlice.l2 {
			if v1 == v2 {
				c += 1
			}
		}
		similarity += v1 * c
	}
	return similarity
}
