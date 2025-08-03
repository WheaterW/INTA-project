dns server source-ip
====================

dns server source-ip

Function
--------



The **dns server source-ip** command configures the source IP address for the DNS client to communicate with a server.

The **undo dns server source-ip** command deletes the source IP address for the DNS client to communicate with a server.



By default, no source IP address is configured for the DNS client to communicate with a server.


Format
------

**dns server source-ip** [ **vpn-instance** *vpn-instance-name* ] *ip-address*

**undo dns server source-ip** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance used by the device to exchange DNS packets. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *ip-address* | Specifies the source IP address for the DNS client to communicate with a server. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a DNS client communicates with a DNS server, you can specify a source IP address for the client to ensure communication security. The route from the DNS server to the specified source IP address must be reachable. The DNS server sends the DNS response packet to the client along the route with the specified source IP address. If you do not specify the source address, the source address is selected based on the destination address each time the client sends a DNS request.

**Precautions**

The source address takes effect immediately after being configured. To ensure normal services, pay attention to the following points:

* If the DNS server has only one reachable route to the specified destination address, you need to specify the source address of the DNS query request sent by the device to the DNS server.
* Ensure that the source IP address is the IP address of an interface or logical interface on the device and that the interface and the DNS server are reachable to each other.
* Ensure that the source address and the DNS server address are on the same VPN or public network.
* If no VPN is specified when you configure the source IP address, the globally configured VPN is used.

Example
-------

# Set the source IP address of the local device in vpn1 to 172.16.1.2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] dns server source-ip vpn-instance vpn1 172.16.1.2

```

# Specify the source IP address 172.16.1.1 for the DNS client to communicate with a server.
```
<HUAWEI> system-view
[~HUAWEI] dns server source-ip 172.16.1.1

```