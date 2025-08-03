source-ip (GRPC server view)
============================

source-ip (GRPC server view)

Function
--------



The **source-ip** command configures a source IPv4 address listened on a gRPC server.

The **undo source-ip** command deletes a source IPv4 address listened on a gRPC server.



By default, no source IPv4 address is configured on a gRPC server.


Format
------

**source-ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ]

**undo source-ip** [ *ip-address* [ **vpn-instance** *vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a source IPv4 address to be listened. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to be bound to the source IPv4 address to be listened. | The value is a string of 1 to 31 case-sensitive characters without spaces.  The value must be the name of an existing VPN instance. |



Views
-----

GRPC server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, on the server, configure a source IPv4 address to be listened and bind it to a VPN instance. A connection can then be established between the server and client.

**Precautions**

To ensure that routes are reachable between the server and client, you can set the source IP address on the server to 0.0.0.0. In this case, the client can certainly establish a connection with the server. If you do not set the source IPv4 address to 0.0.0.0, ensure that it is an existing service interface IP address. In this case, the client establishes a connection with the server based on the source IPv4 address configured.To delete a configured source IPv4 address in the gRPC server view, ensure that the gRPC service is disabled.


Example
-------

# Set the source IPv4 address of the gRPC server to be listened to 10.10.1.2, and set the name of the bound VPN instance to vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 export-extcommunity
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc server
[*HUAWEI-grpc-server] source-ip 10.10.1.2 vpn-instance vpn1

```

# Set the source IPv4 address to be listened during Telemetry dynamic subscription to 10.10.1.2.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server
[~HUAWEI-grpc-server] source-ip 10.10.1.2

```