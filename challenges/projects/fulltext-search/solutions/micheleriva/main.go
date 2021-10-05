package main

import (
	"fmt"

	// cvs "github.com/micheleriva/challenges/src/csv"
	es "github.com/micheleriva/challenges/src/elastic"
)

func init() {
	if !es.IndexExists() {
		fmt.Println("Index does not exists, creating now...")
		es.CreateIndex()
	}
}

func main() {
	// content := cvs.ReadCSVFile()

	indexExists := es.IndexExists()

	fmt.Println(indexExists)
}
