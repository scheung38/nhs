https://stackoverflow.com/questions/17076635/how-to-extract-lines-numbers-that-match-a-regular-expression-in-a-text-file

https://dzone.com/articles/finding-line-number-when

https://gist.github.com/edhiley/fdf7793d3d2c9e838c11

http://forums.devshed.com/python-programming-11/finding-line-regex-found-569121.html

https://developers.google.com/edu/python/regular-expressions#findall

https://stackoverflow.com/questions/469913/regular-expressions-is-there-an-and-operator

http://www.pythonforbeginners.com/regex/regular-expressions-in-python

http://lucumr.pocoo.org/2015/11/18/pythons-hidden-re-gems/

https://github.com/mitsuhiko/python-regex-scanner/blob/master/examples/wiki.py

https://stackoverflow.com/questions/10918682/concatenate-path-platform-independent

https://github.com/tartley/python-regex-cheatsheet/blob/master/cheatsheet.rst

https://www.dotnetperls.com/re-python

https://howchoo.com/g/zdvmogrlngz/python-regexes-findall-search-and-match

https://www.slant.co/versus/9149/9150/~pytest_vs_nose

https://www.youtube.com/watch?v=3oW-hwUvy8A

https://www.youtube.com/watch?v=TuVeWTieJGI

https://www.youtube.com/watch?v=UwCX9oPpfPI&t=516s

https://agopian.info/presentations/2015_06_djangocon_europe/

The match function is used for finding matches at the beginning of a string only.

This search function is very much like match except it looks throughout the entire string and returns the first match.
Taking our example from above:

Acceptance criteria
===================

The acceptance criteria are shown below.


Query                              Type of search   Expected outcome: document
------------------------------------------------------------------------------
Care Quality Commission            OR               0,1,2,3,4,5,6
September 2004                     OR               9
general population generally       OR               6,8
Care Quality Commission admission  AND              1
general population Alzheimer       AND              6