# Connection checker #

The program allows you to check whether a certain URL or a number of URLs is online or not.

The checker uses command line interface and can be provided with several arguments:
Argument | Description
-----|---------
-u | Should be followed by urls to check
-f | Should be followed by the file (only one) containing urls to check
-a | Can be added to conduct checks asynchronously
-t | Measure time it takes to access each website separately and all together

Thus, the example of commands are:
```
python -m Checker -u python.org docs.python.org
python -m Checker -f links.txt -a
python -m Checker -u python.org docs.python.org microsoft.com -a -t
```
