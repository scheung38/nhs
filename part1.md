## Synopsis

Technical test

## Code Example

Part 1 - News search

Create search routines to perform queries on a set of documents defined at https://gist.github.com/edhiley/fdf7793d3d2c9e838c11. The file can be copied locally to your solution for ease of use. The documents are line separated and are referenced in the order they appear, e.g.

News article                        Reference
June 5 , 2013 : The majority ...    0
July 9 , 2013 : The HSCIC has ...   1

The solution must:
be implemented ideally in Python;
pass the acceptance criteria (via unit tests);
not use a library or service to perform the search;
have a command line application that accepts search parameters, and returns the result;
compile (if required) and run on Windows 7 or Ubuntu >= 12.04;
have a README file with instructions on how to run the solution, this should be plain text (markdown) and not a word document;

Acceptance criteria

The acceptance criteria are shown below.

Query                               Type of search      Expected outcome: document references
Care Quality Commission             OR                  0,1,2,3,4,5,6
September 2004                      OR                  9
general population generally        OR                  6,8
Care Quality Commission admission   AND                 1
general population Alzheimer        AND                 6


Part 2 - Riak tasks
The task below should be completed in a markdown file named part2.md, which should be provided in the root directory of your submission.
Please ensure that markdown formatting is followed - please see markdown cheat sheet if required. You will need curl to complete these tasks,
it is not preferred, but acceptable to complete these activities without installing Riak by reading the documentation on Basho's website.
If you do decide to install Riak, there is a 5 minute install guide available.

No code is required to complete this section, just the curl request examples.
Provide appropriate titles and short descriptions in your markdown file.
Please state if completed without Riak being available.

If Riak is used, please supply the version in the file part2.md.
Common query caching
Imagine that the 'news search' functionality in Part 1 is now live, and through analytics it is known that the top 5 queries of the system
comprise around 90% of all search queries. A useful optimisation is to store the results to common queries in Riak. This task is to show
how this cache can be created.

The solution must:
provide curl requests that will create a cache of the result in Riak for the top 5 queries;
assume that the top 5 queries and results are the same as the acceptance criteria in Part 1;
provide an example curl GET request that uses the inserted data to retrieve the cached result of the OR query: 'Care Quality Commission';
use correct HTTP methods for curl requests;
use the correct content type for how you want to store the data.

Monthly indexes
The analytics show another optimisation is to be able to return results by month/year, to optimise the amount of data that is being queried at any one time.
Making use of a suitable indexing strategy (for example, secondary indexing), write curl requests that will insert each of the documents to be searched into Riak, while allowing for them to be queried by month/year.
An example insert is provided below (without indexes). The document is truncated reasons of brevity. It is acceptable to do so in your response also.

curl -XPUT   -H "Content-Type: text/plain"  \
             -d "April 15 , 2013 Thousands of GP practices ..." \
             http://localhost:8098/buckets/hscicNews/keys/RESULT:5

The solution must:

have curl requests to insert data and indexes;
have example curl GET requests for retrieving the keys of documents by month/year, specifically for June 2013, where the keys for documents 0,2,3 and 4 should be returned;
be possible to retrieve the search text by the keys returned, as in, the original text must be stored;
use correct HTTP methods for curl requests;
use the correct content type for how you want to store the data.
Considerations
Please describe any non-functional considerations you would make to support the above cache and documents.
This can include:
Bucket types,
n-vals,
Riak backend,
Replication

## Motivation


## Installation

$ pip install -r requirements.txt


## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

$ pytest - to run the tests

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)







