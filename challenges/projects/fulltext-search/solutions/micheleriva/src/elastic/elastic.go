package elastic

import (
	"context"
	"encoding/json"
	"fmt"

	csv "github.com/micheleriva/challenges/src/csv"
	"github.com/olivere/elastic/v7"
	"github.com/olivere/elastic/v7/config"
)

type Quote struct {
	Quote  string `json:"quote"`
	Author string `json:"author"`
}

const IndexName = "quotes"
const IndexMapping = `
{
	"mappings": {
		"properties": {
			"quote": {
				"type": "text"
			},
			"author": {
				"type": "text"
			},
			"suggest_field": {
				"type": "completion"
			}
		}
	}
}
`

var client *elastic.Client

func init() {
	conf, _ := config.Parse("http://localhost:9200?sniff=false")

	esClient, err := elastic.NewClientFromConfig(conf)
	if err != nil {
		panic(err)
	}

	client = esClient

	createIndex()
}

func createIndex() {
	ctx := context.Background()
	exists, err := client.IndexExists(IndexName).Do(ctx)
	if err != nil {
		panic(err)
	}

	if !exists {
		fmt.Println("Index does not exists. Creating...")
		createIndex, err := client.CreateIndex(IndexName).BodyString(IndexMapping).Do(ctx)
		if err != nil {
			panic(err)
		}

		if !createIndex.Acknowledged {
			panic("Not acknowledged")
		}
	}
}

func ImportContent(quotes []csv.CSVContent) error {
	ctx := context.Background()

	for _, quote := range quotes {
		put, err := client.
			Index().
			Index(IndexName).
			Type("_doc").
			BodyJson(quote).
			Do(ctx)

		if err != nil {
			return err
		}

		fmt.Printf("Indexed %s\n", put.Id)
	}

	return nil
}

func Search(query string, size int, from int) ([]Quote, error) {
	ctx := context.Background()

	var mustQueries []elastic.Query

	boolQuery := elastic.NewBoolQuery()
	mustQueries = append(mustQueries, elastic.NewQueryStringQuery(query))

	boolQuery.Must(mustQueries...)

	res, err := client.
		Search().
		Index(IndexName).
		Type("_doc").
		Size(size).
		From(from).
		Query(boolQuery).
		Do(ctx)

	if err != nil {
		return nil, err
	}

	var quotes []Quote

	for _, hit := range res.Hits.Hits {
		var quote Quote
		err := json.Unmarshal(hit.Source, &quote)
		if err != nil {
			return nil, err
		}

		quotes = append(quotes, quote)
	}

	return quotes, nil
}
