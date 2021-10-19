package controller

import (
	"strconv"

	"github.com/gin-gonic/gin"
	es "github.com/micheleriva/challenges/src/elastic"
)

func QueryController(c *gin.Context) {
	q := c.Query("q")
	limit := c.Query("limit")
	from := c.Query("from")

	if q == "" {
		c.JSON(422, gin.H{
			"error": "Missing 'q' param",
		})
	}

	if limit == "" {
		c.JSON(422, gin.H{
			"error": "Missing 'limit' param",
		})
	}

	if from == "" {
		c.JSON(422, gin.H{
			"error": "Missing 'from' param",
		})
	}

	limitInt, err := strconv.Atoi(limit)
	if err != nil {
		c.JSON(500, gin.H{
			"error": "Internal server error",
		})
	}

	fromInt, err := strconv.Atoi(from)
	if err != nil {
		c.JSON(500, gin.H{
			"error": "Internal server error",
		})
	}

	results, err := es.Search(q, limitInt, fromInt)
	if err != nil {
		c.JSON(500, gin.H{
			"error": "Internal server error",
		})
	}

	c.JSON(200, gin.H{
		"result": results,
	})
}
