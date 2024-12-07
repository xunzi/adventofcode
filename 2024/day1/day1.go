package main

import (
	"flag"
	"fmt"
	"log"
)

func main() {
	var sSlice = sortedSlices{}
	infile := flag.String("infile", "input", "input file")
	flag.Parse()
	lines, err := ingestDestinationFile(*infile)

	if err != nil {
		log.Fatalf("Error ingesting: %s", err)
	}
	sSlice = covertToSortedSlices(lines)
	fmt.Println("Part1: ", sSlice.Distances())
	fmt.Println("Part 2: ", sSlice.Similarity())
}
