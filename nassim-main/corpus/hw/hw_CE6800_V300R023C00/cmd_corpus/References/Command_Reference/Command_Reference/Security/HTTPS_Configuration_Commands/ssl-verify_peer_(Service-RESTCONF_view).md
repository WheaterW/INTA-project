ssl-verify peer (Service-RESTCONF view)
=======================================

ssl-verify peer (Service-RESTCONF view)

Function
--------



The **ssl-verify peer** command configures an HTTP server to perform SSL verification on HTTP clients.

The **undo ssl-verify** command disables an HTTP server from performing SSL verification on HTTP clients.



By default, an HTTP server does not perform SSL verification on HTTP clients.


Format
------

**ssl-verify peer**

**undo ssl-verify**


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

To prevent access of unauthorized HTTP clients, run the ssl-verify-mode command to configure an HTTP server to perform SSL verification on HTTP clients. This configuration enhances security.

**Precautions**

If a client does not have a certificate loaded or has an incorrect certificate loaded, the verification fails, and the server disconnects the client.


Example
-------

# Configure an HTTP server to perform forcible SSL verification on HTTP clients.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy a
[*HUAWEI-ssl-policy-a] quit
[*HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] secure-server enable
[*HUAWEI-http-service-restconf] ssl-policy a
[*HUAWEI-http-service-restconf] ssl-verify peer

```