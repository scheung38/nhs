## Motivation

## Installation

Need to modify riak.conf to change backend type and to turn on Riak UI

/usr/local/Cellar/riak/2.2.3/libexec/etc


Command line to initially define bucket type

$ riak-admin bucket-type create news '{"props":{"search_index":"year"}}'

storage_backend = memory

then

$ riak restart -> ok


$ riak version
2.2.3


Riak UI Panel is available on

http://127.0.0.1:8098/admin#/cluster








