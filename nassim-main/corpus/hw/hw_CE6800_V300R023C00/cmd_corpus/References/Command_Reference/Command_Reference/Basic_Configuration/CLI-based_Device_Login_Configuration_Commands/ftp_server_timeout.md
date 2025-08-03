ftp server timeout
==================

ftp server timeout

Function
--------



The **ftp server timeout** command sets the idle timeout interval of the client.

The **undo ftp server timeout** command restores the idle timeout interval to its default value.



By default, the timeout value is 10 minutes.


Format
------

**ftp server timeout** *minutes*

**undo ftp server timeout**


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

**Usage Scenario**



The timeout interval is set to disconnect the services provided by the FTP server to the client, which is idle for the specified time.The command ftp server timeout only takes effect for ipv4 connection.




Example
-------

# Set the timeout interval to 50 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ftp server timeout 50

```