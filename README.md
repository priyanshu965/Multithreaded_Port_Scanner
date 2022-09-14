# Multithreaded_Port_Scanner
A Port Scanner with Multi-Threading And User Define Port Range in Python

# Installation
```
git clone https://github.com/priyanshu965/Multithreaded_Port_Scanner
cd Multithreaded_Port_Scanner
python port_Scanner.py
```

# Usage
```
usage: port_Scanner.py 192.168.120.155

Advance Port Scanner

positional arguments:
IPv4                  Target

options:
  -h, --help            show this help message and exit
  -s, --start START     Starting Point (Default value is 1)
  -e, --end END         Ending Port (Default value is 65535)
  -t, --thread THREAD   Number Of Threads
  -v, --verbose         Verbose Mode

```

*Note:* Default Thread value is `500` & It can be change using `-t`.

- If the port is not specified then it will scan all the ports from 1-65535. 
