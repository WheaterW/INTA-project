permit no-tls
=============

permit no-tls

Function
--------



The **permit no-tls** command configures a security policy for a gRPC server to allow selected services to run on an unencrypted gRPC channel.

The **undo permit no-tls** command restores the default security policy of a gRPC server.



By default, services are not allowed to run on an unencrypted gRPC channel.


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

GRPC server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **permit no-tls** command configures a security policy for a gRPC server to allow selected services to run on an unencrypted gRPC channel.

**Precautions**

If an SSL policy has been configured on the gRPC server, services can run only on an encrypted gRPC channel.If no SSL policy is configured on the gRPC server, the connections that are established for services after the **permit no-tls** command is run will be disconnected after the **undo permit no-tls** command is run.


Example
-------

# Allow services to run on an unencrypted gRPC channel.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server
[~HUAWEI-grpc-server] permit no-tls gnmi
Warning: If no SSL policy is configured, the selected service is allowed to run. Continue? [Y/N]:y
[*HUAWEI-grpc-server]

```