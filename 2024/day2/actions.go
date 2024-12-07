package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func verifyReport(report []int) bool {
	ret := true
	switch {
	case report[1] > report[0]:
		for i, v := range report[1:] {
			i = i + 1
			//fmt.Println(v, report[i-1])
			if v <= report[i-1] {
				ret = false
			}
			if abs(v-report[i-1]) > 3 {
				return false
			}
		}
	case report[1] < report[0]:
		for i, v := range report[1:] {
			i = i + 1
			//fmt.Println(v, report[i-1])
			if v >= report[i-1] {
				ret = false
			}
			if abs(v-report[i-1]) > 3 {
				return false
			}
		}
	case report[1] == report[0]:
		ret = false
	}
	return ret
}

func ingestData(infile string) ([]string, error) {
	fileHandle, err := os.Open(infile)
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

func createReports(strReports []string) [][]int {
	var intReports [][]int
	for _, line := range strReports {
		var intLine []int
		for _, field := range strings.Fields(line) {
			i, _ := strconv.Atoi(field)
			intLine = append(intLine, i)
		}
		intReports = append(intReports, intLine)
	}
	return intReports
}

func removeIndex(intSlice []int, idx int) []int {
	ret := make([]int, 0)
	ret = append(ret, intSlice[:idx]...)
	ret = append(ret, intSlice[idx+1:]...)
	//fmt.Println(intSlice, ret)
	return ret
}

func applyDampener(report []int) bool {
	ret := false
	for i, _ := range report {
		reducedReport := removeIndex(report, i)
		if verifyReport(reducedReport) {
			//fmt.Println(report, reducedReport, verifyReport(reducedReport))
			return true
		}
	}
	return ret
}
