# Computing Metrics from Input Lines

This script reads from stdin line by line and computes metrics based on the input format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints the following statistics from the beginning:

- Total file size: \<total size\>, where \<total size\> is the sum of all previous \<file size\> (see input format above)
- Number of lines by status code:
  - Possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  - If a status code doesn’t appear or is not an integer, it will not be printed for this status code
