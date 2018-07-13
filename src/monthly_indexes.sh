curl -v -X PUT \
  --header 'cache-control: cache' \
  --header 'content-type: application/json'  \
  --data "{"props":{"search_index":"year"}}" \
  --data "{"props":{"search_index":"month"}}" \
  --url http://localhost:8098/types/news/buckets/hscicNews/props




