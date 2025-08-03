http server ip-block disable
============================

http server ip-block disable

Function
--------



The **http server ip-block disable** command disables an HTTP server from locking client IP addresses.

The **undo http server ip-block disable** command enables an HTTP server to lock client IP addresses.



By default, an HTTP server is enabled to lock client IP addresses.


Format
------

**http server ip-block disable**

**undo http server ip-block disable**


Parameters
----------

None

Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* When the client IP address locking function is enabled on the HTTP server, the client IP address is locked if the client fails to log in to the server for multiple times. During the locking period, the client cannot log in to the server. You can run the **display ssh server ip-block list** command to query the locked client IP address.
* When the client IP address locking function is disabled on the HTTP server, the client IP address is not locked even if the client fails to log in to the server for multiple times.

**Precautions**

Disabling this function poses security risks to the system. Therefore, you are advised not to disable the IP address locking function.


Example
-------

# Disable an HTTP server from locking client IP addresses.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] http server ip-block disable

```