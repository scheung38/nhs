## Motivation

## Installation and Initial Setup

Need to modify riak.conf to change backend type and to turn on Riak UI

/usr/local/Cellar/riak/2.2.3/libexec/etc

Command line to initially define bucket type as Python client API cannot define it

$ riak-admin bucket-type create news '{"props":{"search_index":"year"}}'

storage_backend = memory

## Launch riak

$ riak restart -> ok


## Version

$ riak version -> 2.2.3

http://localhost:8098/buckets/hscicNews/keys/RESULT

Riak UI Panel is available on

http://127.0.0.1:8098/admin#/cluster








