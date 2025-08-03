ftp ipv6 server timeout
=======================

ftp ipv6 server timeout

Function
--------



The **ftp ipv6 server timeout** command sets the idle timeout interval of the client.

The **undo ftp ipv6 server timeout** command restores the idle timeout interval to its default value.



By default, the timeout value is 10 minutes.


Format
------

**ftp ipv6 server timeout** *minutes*

**undo ftp ipv6 server timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *minutes* | Specifies the timeout interval in minutes. | Timeout interval is an integer data type. The value range is from 1 to 35791 minutes. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The timeout interval is set to disconnect the services provided by the FTP server to the client, which is idle for the specified time.


Example
-------

# Set the timeout interval to 50 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ftp ipv6 server timeout 50

```