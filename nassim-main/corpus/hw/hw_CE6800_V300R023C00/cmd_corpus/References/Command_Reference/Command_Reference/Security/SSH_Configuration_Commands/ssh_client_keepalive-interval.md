ssh client keepalive-interval
=============================

ssh client keepalive-interval

Function
--------



The **ssh client keepalive-interval** command configures the keepalive interval on the SSH client.

The **undo ssh client keepalive-interval** command restores the default configuration.



By default, the keepalive interval is set to zero seconds.


Format
------

**ssh client keepalive-interval** *seconds*

**undo ssh client keepalive-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *seconds* | Specifies a keepalive interval, in seconds. | It is an integer data type. The keepalive interval range is from 0 to 3600 seconds. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The client sends a keepalive message to the server, if it does not receive any data for the keepalive interval from the server. The keepalive messages are sent after the expiry of the keepalive interval. The client disconnects the current connection in case of server response failure.If you reset the keepalive interval to zero seconds, the client does not send any keepalive messages to the server.This command takes effect for both IPv4 and IPv6 SSH clients.


Example
-------

# Configure the keepalive-interval to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ssh client keepalive-interval 30

```