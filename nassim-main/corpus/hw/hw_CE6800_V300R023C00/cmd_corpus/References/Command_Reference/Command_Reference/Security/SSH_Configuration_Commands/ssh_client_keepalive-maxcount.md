ssh client keepalive-maxcount
=============================

ssh client keepalive-maxcount

Function
--------



The **ssh client keepalive-maxcount** command configures the maximum number of keepalive messages sent by an SSH client.

The **undo ssh client keepalive-maxcount** command restores the default configuration.



By default, the maximum number of keepalive messages is set to 3.


Format
------

**ssh client keepalive-maxcount** *count*

**undo ssh client keepalive-maxcount**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *count* | Specifies the maximum number of keepalive messages. | It is an integer data type. The value ranges from 1 to 30. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* The client sends keepalive messages to the server. If the client does not receive any data within the keepalive interval from the server, the client sends the keepalive message up to the configured maximum number. The client disconnects the current connection in case of server response failure.
* The client kept on sending the keepalive message to the server up to the configured maximum number. The client disconnects the current connection on failure of server response.
* The keepalive interval configuration overrides the keepalive maximum number configuration. For example, If the keepalive interval is set to zero seconds (does not send keepalive messages), the keepalive maximum number configuration has no effect.
* This command takes effect for both IPv4 and IPv6 SSH clients.


Example
-------

# Set the maximum number of keepalive messages sent by an SSH client to 5.
```
<HUAWEI> system-view
[~HUAWEI] ssh client keepalive-maxcount 5

```