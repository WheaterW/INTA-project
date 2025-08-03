ssl-verify peer (GRPC IPv6 server view)
=======================================

ssl-verify peer (GRPC IPv6 server view)

Function
--------



The **ssl-verify peer** command enables a server to perform SSL verification on a client during Telemetry dynamic subscription.

The **undo ssl-verify peer** command disables a server from performing SSL verification on a client during Telemetry dynamic.



By default, the gRPC IPv6 server does not perform SSL verification on the client during Telemetry dynamic subscription.


Format
------

**ssl-verify peer**

**undo ssl-verify peer**


Parameters
----------

None

Views
-----

GRPC IPv6 server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The server performs SSL verification on a client based on the specified SSL policy. If the client does not have a certificate or the certificate is incorrect, the server disconnects from the client.


Example
-------

# Configure the gRPC IPv6 server to perform SSL verification on the client during Telemetry dynamic subscription.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[*HUAWEI-ssl-policy-policy1] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc server ipv6
[*HUAWEI-grpc-server-ipv6] ssl-verify peer

```