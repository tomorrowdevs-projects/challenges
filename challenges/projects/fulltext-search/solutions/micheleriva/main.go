package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
	"github.com/micheleriva/challenges/src/controller"
	"github.com/micheleriva/challenges/src/elastic"
)

func main() {
	results, err := elastic.Search("horror", 10, 0)
	if err != nil {
		fmt.Println("We got an error:")
		fmt.Println(err)
	}

	for _, result := range results {
		fmt.Println(result.Author)
	}

	router := gin.Default()
	router.GET("/elastic", controller.QueryController)

	router.Run("localhost:8081")
}
