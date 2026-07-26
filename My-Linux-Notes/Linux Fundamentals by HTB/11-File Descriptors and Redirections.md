
**Date:** 26-07-2026
**Tags:** 

# Definition:
- A file descriptor (`FD`) in Unix/Linux operating systems is a reference, maintained by the kernel, that allows the system to manage Input/Output (`I/O`) operations. It acts as a unique identifier for an open file, socket, or any other I/O resource. In Windows-based operating systems, this is known as a file handle. Essentially, the file descriptor is the system's way of keeping track of active `I/O` connections, such as reading from or writing to a file.
- By default, the first three file descriptors in Linux are:
1. Data Stream for Input `STDIN - 0` 
2. Data Stream for Output `STDOUT - 1` 
3. Data Stream for Output that relates to an error occurring `STDERR - 2` 

