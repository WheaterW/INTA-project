ssl-verify peer (GRPC client view)
==================================

ssl-verify peer (GRPC client view)

Function
--------



The **ssl-verify peer** command configures an SSL policy for a client.

The **undo ssl-verify peer** command deletes the SSL policy configured for a client.



By default, a client does not perform SSL verification on a server.


Format
------

**ssl-verify peer**

**undo ssl-verify peer**


Parameters
----------

None

Views
-----

GRPC client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When you create a gRPC-based static subscription, you can run the **ssl-verify peer** command to enable a client to perform SSL verification on a server. If the server does not have a certificate or the certificate is incorrect, the client tears down the connection with the server.

**Precautions**

If the no-tls parameter has been configured by running the **ipv4-address port** or **ipv6-address port** command in the destination group view or **protocol** command in the subscription view and taken effect, the TLS encryption mode is not used. In this case, the configuration that enables the client to perform SSL verification on a server does not take effect.


Example
-------

# Enable a client to perform SSL verification on a server during Telemetry static subscription.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc client
[~HUAWEI-grpc-client] ssl-verify peer

```