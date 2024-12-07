package main

import (
	"flag"
	"fmt"
	"log"
)

func main() {
	infile := flag.String("infile", "input", "input file")
	flag.Parse()
	safeCount := 0
	strReports, err := ingestData(*infile)
	if err != nil {
		log.Fatalf("Error ingesting: %v", err)
	}
	//fmt.Print(len(strReports))
	intReports := createReports(strReports)
	//fmt.Printf("%v", intReports)
	for _, rep := range intReports {
		//fmt.Println(rep, verifyReportIncDec(rep))
		if verifyReport(rep) {
			safeCount += 1
			continue
		}
		fmt.Println(rep, applyDampener(rep))
	}
	fmt.Println("Part 1", safeCount)
}
