peer-address
============

peer-address

Function
--------



The **peer-address** command configures an IP address, a port number, and a VPN instance for a destination group of a gRPC client.

The **undo peer-address** command deletes the IP address, port number, and VPN instance of a destination group of a gRPC client.



By default, no IP address, port number, or VPN instance is configured for a destination group of a gRPC client.


Format
------

**peer-address ipv4** *ip-address-ipv4* **port** *port-value* [ **vpn-instance** *vpn-name* ]

**peer-address ipv6** *ip-address-ipv6* **port** *port-value* [ **vpn-instance** *vpn-name* ]

**undo peer-address ipv4** *ip-address-ipv4* **port** *port-value* [ **vpn-instance** *vpn-name* ]

**undo peer-address ipv6** *ip-address-ipv6* **port** *port-value* [ **vpn-instance** *vpn-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **port** *port-value* | Specifies the port number of the destination group. | The value is an integer ranging from 1 to 65535. |
| **vpn-instance** *vpn-name* | Specifies the name of the VPN instance to which the destination group belongs. | The value is a string of 1 to 31 characters. The value must be the name of an existing VPN instance on the device. |
| **ipv6** *ip-address-ipv6* | Specifies the IPv6 address of the destination group. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **ipv4** *ip-address-ipv4* | Specifies the IPv4 address of the destination group. | The value is in dotted decimal notation. |



Views
-----

grpc-client-destination-group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a destination group is created for a gRPC client, run this command to configure an IP address, a port number, and a VPN instance for the destination group.

**Precautions**

Only one group of IP addresses, port numbers, and VPN instances can be configured for each gRPC client destination group.


Example
-------

# Set the IP address and port number of the destination group for the gRPC client to 10.1.1.1 and 10001, respectively.
```
<HUAWEI> system-view
[~HUAWEI] grpc
[~HUAWEI-grpc] grpc client
[~HUAWEI-grpc-client] destination-group dest
[*HUAWEI-grpc-client-destination-group-dest] peer-address ipv4 10.1.1.1 port 10001

```