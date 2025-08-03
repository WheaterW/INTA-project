secure-server port
==================

secure-server port

Function
--------



The **secure-server port** command configures an HTTPS service listening port.

The **undo secure-server port** command restores the default HTTPS service listening port.



By default, HTTPS service listening uses port 443.


Format
------

**secure-server port** *port-number-secure*

**undo secure-server port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-number-secure* | Specifies the number for an HTTPS service listening port. | The value can be 443 or an integer ranging from 1025 to 65535. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* If the default HTTPS service listening port is in use, run the **secure-server port** command to change the HTTPS service listening port so that an ACL can be used to filter packets on this port, improving network packet security.
* Currently, only the IPv4 port number of the HTTPS service can be configured.
* The port number that is being used cannot be configured.

Example
-------

# Configure port 1028 for HTTPS listening.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] secure-server port 1028

```