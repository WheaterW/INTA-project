source-ip (GRPC IPv6 server view)
=================================

source-ip (GRPC IPv6 server view)

Function
--------



The **source-ip** command configures a source IPv6 address listened on a gRPC server.

The **undo source-ip** command deletes a source IPv6 address listened on a gRPC server.



By default, no source IPv6 address is configured on a gRPC server.


Format
------

**source-ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ]

**undo source-ip** [ *ip-address* [ **vpn-instance** *vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a source IPv6 address to be listened. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to be bound to the source IPv6 address to be listened. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

GRPC IPv6 server view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a collector functioning as a client initiates a connection to a device functioning as a server, the data sampled is dynamically subscribed to. In this case, on the server, configure a source IPv6 address to be listened and the name of a VPN instance to be bound to the source IPv6 address. A connection can then be established between the server and client.

**Precautions**

To delete a configured source IPv6 address in the gRPC IPv6 server view, ensure that the gRPC IPv6 service is disabled.


Example
-------

# Set the source IPv6 address of the gRPC server to be listened to 2001:DB8:2::1, and set the name of the bound VPN instance to vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] vpn-target 2:2 export-extcommunity
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] grpc
[*HUAWEI-grpc] grpc server ipv6
[*HUAWEI-grpc-server-ipv6] source-ip 2001:DB8:2::1 vpn-instance vpn1

```

# Set the source IPv6 address of the gRPC server to be listened to 2001:DB8:2::1.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc server ipv6
[~HUAWEI-grpc-server-ipv6] source-ip 2001:DB8:2::1

```