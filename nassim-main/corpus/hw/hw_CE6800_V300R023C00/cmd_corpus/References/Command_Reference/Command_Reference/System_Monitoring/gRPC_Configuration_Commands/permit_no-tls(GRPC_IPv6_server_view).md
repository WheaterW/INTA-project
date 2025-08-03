permit no-tls(GRPC IPv6 server view)
====================================

permit no-tls(GRPC IPv6 server view)

Function
--------



The **permit no-tls** command configures a security policy for a gRPC IPv6 server to allow selected services to run on an unencrypted gRPC IPv6 channel.

The **undo permit no-tls** command restores the default security policy of a gRPC IPv6 server.



By default, services are not allowed to run on an unencrypted gRPC IPv6 channel.


Format
------

**permit no-tls** { **gnmi** }

**undo permit no-tls** { **gnmi** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **gnmi** | Indicates the gNMI protocol. | - |



Views
-----

GRPC IPv6 server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **permit no-tls** command configures a security policy for a gRPC IPv6 server to allow selected services to run on an unencrypted gRPC IPv6 channel.

**Precautions**

If an SSL policy has been configured on the gRPC IPv6 server, services can run only on an encrypted gRPC IPv6 channel.If no SSL policy is configured on the gRPC IPv6 server, the connections that are established for services after the **permit no-tls** command is run will be disconnected after the **undo permit no-tls** command is run.


Example
-------

# Allow services to run on an unencrypted gRPC IPv6 channel.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server ipv6
[~HUAWEI-grpc-server-ipv6] permit no-tls gnmi
Warning: If no SSL policy is configured, the selected service is allowed to run. Continue? [Y/N]:y
[*HUAWEI-grpc-server-ipv6]

```