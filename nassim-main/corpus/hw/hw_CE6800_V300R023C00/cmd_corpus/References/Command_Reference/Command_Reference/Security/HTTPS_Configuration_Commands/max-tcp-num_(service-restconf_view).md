max-tcp-num (service-restconf view)
===================================

max-tcp-num (service-restconf view)

Function
--------



The **max-tcp-num** command configures the maximum number of TCP connections to HTTP server for each IP address.

The **undo max-tcp-num** command restores the default value to the number of TCP connections to HTTP server for each IP address.



By default, the maximum number of connections for each IP address is 30.


Format
------

**max-tcp-num** *num*

**undo max-tcp-num**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *num* | Configure the maximum number of connections for each IP address. | The value is an integer ranging from 1 to 30. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When the device functions as an HTTP server, a maximum of 30 TCP connections can be established to the server for each IP address. This prevents other clients from connecting to the server due to malicious connections.


Example
-------

# Set the maximum number of connections for a single IP address to 25.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] max-tcp-num 25

```