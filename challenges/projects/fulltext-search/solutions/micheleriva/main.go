package main

import (
	es "github.com/micheleriva/challenges/src/elastic"
)

func main() {
	elastic := es.Init()

	elastic.Indices.Create("quotes")
}
