# Full-Text Search

Implement a full-text search REST API using Elastic Search.

# API Schema

The REST API must implement the following schema:

## Get all quotes from a given author

**Endpoint**: `GET /api/v1/by-author`

**Query Parameters**

| key | type | mandatory |
|-----|------|-----------|
| `author` | string | yes |
| `limit` | integer | no |
| `offset`| integer | no |

**Response**

```json
{
  "quotes": ["quote1", "quote2"],
  "total": // total number of quotes
}
```

**Example call**

`curl -X GET http://localhost/api/v1/by-author?author=Michelangelo&limit=3&offset=0`

```json
{
  "quotes": [
    "The greater danger for most of us lies not in setting our aim too high and falling short; but in setting our aim too low, and achieving our mark.",
    "The true work of art is but a shadow of the divine perfection",
    "I saw the angel in the marble and carved until I set him free"
  ],
  "total": 26
}
```

## Get all quotes containing a given word

**Endpoint**: `GET /api/v1/search`

**Query Parameters**

| key | type | mandatory |
|-----|------|-----------|
| `term` | string | yes |
| `limit` | integer | no |
| `offset`| integer | no |

**Response**

```json
{
  "quotes": [
    {
      "author": "",
      "quote": ""
    },
    {
      "author": "",
      "quote": ""
    }
  ],
  "total": // total number of quotes
}
```

**Example call**

`curl -X GET http://localhost/api/v1/search?term=heart&limit=2&offset=0`

**Response**

```json
{
  "quotes": [
    {
      "author": "Abel Ferrara",
      "quote": "Mulberry Street was the beating heart of the Italian-American experience, but you don't find those gangsters now. I live with a bunch of yuppies and models."
    },
    {
      "author": "Aberjhani",
      "quote": "At some point, a flash of sustained clarity reveals the difference between what someone would have you believe is true, and what you know from the depths of your own heart to the peaks of your soul to be true. What happens after that is up to you."
    }
  ],
  "total": 592
}
```

# Technical requirements

It must be implemented using the [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/client/java-api/current/index.html) client. <br />
You can use a programming language of your choice.