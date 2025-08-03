server port
===========

server port

Function
--------



The **server port** command configures an HTTP service listening port.

The **undo server port** command restores the default HTTP service listening port.



By default, HTTP service listening uses port 80.


Format
------

**server port** *port-number*

**undo server port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number* | Specifies the number for an HTTP service listening port. | The value can be 80 or an integer ranging from 1025 to 65535. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* When the default HTTP listening port number is occupied, run the **server port** command to change the HTTP listening port number so that packets can be filtered based on the port number, improving network packet security.
* Currently, only the IPv4 port number of the HTTP service can be configured.
* The port number that is being used cannot be configured.

Example
-------

# Configure port 1028 for HTTP service listening.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] server port 1028

```