$ riak version
2.2.3

$ riak start


$ riak stop


riak.conf

/usr/local/Cellar/riak/2.2.3/libexec/etc


Riak UI Panel is available on

riak-admin bucket-type create news '{"props":{"search_index":"year"}}'



http://127.0.0.1:8098/admin#/cluster

storage_backend = bitcask

riak restart -> ok

riak.riak_error.RiakError: '{error,{indexes_not_supported,riak_kv_bitcask_backend}}'



storage_backend = leveldb

riak restart -> ok

riak.riak_error.RiakError: 'all_nodes_down'


storage_backend = multi

riak restart -> ok

socket.error: [Errno 61] Connection refused



storage_backend = prefix_multi

riak restart -> ok

socket.error: [Errno 61] Connection refused



storage_backend = memory worked

riak restart -> ok