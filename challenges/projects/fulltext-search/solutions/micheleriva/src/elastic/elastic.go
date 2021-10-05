package elastic

import (
	"fmt"

	"github.com/elastic/go-elasticsearch/v7"
)

type IndexStruct = struct {
	Author string `json:"author"`
	Quote  string `json:"quote"`
}

const IndexName = "quotes"

var Elastic *elasticsearch.Client

func initializeInstance() *elasticsearch.Client {
	es, err := elasticsearch.NewDefaultClient()
	if err != nil {
		panic(err)
	}

	return es
}

func init() {
	Elastic = initializeInstance()
}

func IndexExists() bool {
	exists, err := Elastic.Indices.Exists([]string{IndexName})
	if err != nil {
		panic(err)
	}

	return exists.StatusCode != 404
}

func CreateIndex() error {
	res, err := Elastic.Indices.Create(IndexName)
	if err != nil {
		return err
	}

	if res.StatusCode != 200 {
		return fmt.Errorf("Index not created")
	}

	return nil
}
