# When to use a queue


	- Queues are particularly useful when you want to process a generic task in sequential order.
	- Queue is used when things don’t have to be processed immediately, but have to be processed in First In First Out order
	- Queue is useful when data is transferred asynchronously between two processes.
	- For example when you process the requests on a a server, you can process the first,`enqueue` the others requests in arriving order, and process them sequentially. If a request errors out when talking to the server, we can re-enqueue it to be tried again.