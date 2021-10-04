package csv

import (
	"encoding/csv"
	"os"
)

type CSVContent struct {
	Author string
	Quote  string
}

func ReadCSVFile() []CSVContent {
	csvFileContent, err := os.Open("QUOTE.csv")
	if err != nil {
		panic(err)
	}
	defer csvFileContent.Close()

	csvLines, err := csv.NewReader(csvFileContent).ReadAll()
	if err != nil {
		panic(err)
	}

	var quotes []CSVContent

	for _, line := range csvLines {
		quote := CSVContent{
			Author: line[0],
			Quote:  line[1],
		}

		quotes = append(quotes, quote)
	}

	return quotes
}
