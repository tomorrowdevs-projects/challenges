package main

import (
	"fmt"

	es "github.com/micheleriva/challenges/src/elastic"
)

func main() {
	results, err := es.Search("horror", 10, 0)
	if err != nil {
		fmt.Println("We got an error:")
		fmt.Println(err)
	}

	for _, result := range results {
		fmt.Println(result.Quote)
	}
}
