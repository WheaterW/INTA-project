server enable (GRPC IPv6 server view)
=====================================

server enable (GRPC IPv6 server view)

Function
--------



The **server enable** command enables the gRPC service.

The **undo server enable** command disables the gRPC service.



By default, the gRPC service is disabled.


Format
------

**server enable**

**undo server enable**


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

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, you need to enable the gRPC service on the server.

**Prerequisites**

The gRPC service listens to a specified source IP address. Therefore, before enabling the gRPC service, you must run the **source-ip** command to configure a source address to be listened.

**Precautions**

To delete a configured source address, ensure that the gRPC service is disabled.


Example
-------

# Enable the gRPC IPv6 service.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server ipv6
[~HUAWEI-grpc-server-ipv6] source-ip 2001:db8:2::2
[~HUAWEI-grpc-server-ipv6] server enable

```