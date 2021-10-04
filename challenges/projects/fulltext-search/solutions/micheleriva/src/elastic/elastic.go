package elastic

import "github.com/elastic/go-elasticsearch/v7"

func Init() *elasticsearch.Client {
	es, err := elasticsearch.NewDefaultClient()
	if err != nil {
		panic(err)
	}

	return es
}
