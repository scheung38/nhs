curl -v -X GET \
  --header 'cache-control: cache' \
  --header 'content-type: application/json' \
  --url http://localhost:8098/types/news/buckets/hscicNews/keys/RESULT

#[[0, 1, 2, 3, 4, 5, 6], [9], [6, 8], [1], [6]]
