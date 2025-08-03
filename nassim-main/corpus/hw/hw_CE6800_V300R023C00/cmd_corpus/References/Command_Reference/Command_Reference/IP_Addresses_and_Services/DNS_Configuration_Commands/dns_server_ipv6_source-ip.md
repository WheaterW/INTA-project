dns server ipv6 source-ip
=========================

dns server ipv6 source-ip

Function
--------



The **dns server ipv6 source-ip** command configures the source IPv6 address for the local end functioning as the DNS client to communicate with the IPv6 DNS server.

The **undo dns server ipv6 source-ip** command deletes the source IPv6 address for the local end functioning as the DNS client to communicate with the IPv6 DNS server.



By default, no source IPv6 address is configured for the local end functioning as the DNS client to communicate with the IPv6 DNS server.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dns server ipv6 source-ip** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address*

**undo dns server ipv6 source-ip** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *ipv6-address* | Specifies the source IPv6 address of the local device. | The value is a 128-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X, with each X representing four hexadecimal numbers. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the device functions as a DNS client, you can specify the source IPv6 address of the local device. The device uses the specified source IPv6 address to communicate with the DNS server with the IPv6 address to ensure security. The DNS server returns the request for a domain name to the local device along the specified route. If no source IPv6 address is configured, the source address is selected based on the destination address each time the client sends a DNS domain name request.

**Precautions**

The source address takes effect immediately after being configured. To ensure normal services, pay attention to the following points:

* If the DNS server has only one reachable route to the specified destination IPv6 address, you need to specify the source IPv6 address in the DNS query request sent from the device to the DNS server.
* Ensure that the source IPv6 address is the IPv6 address of an interface or logical interface on the device, and there are reachable routes between the interface and the DNS server.
* Ensure that the source IPv6 address and the IPv6 address of the DNS server are on the same VPN or public network.
* If no VPN instance is specified when you configure the source IPv6 address, the globally configured VPN instance is used.

Example
-------

# Set the source IPv6 address of the local device to fc00:1::1.
```
<HUAWEI> system-view
[~HUAWEI] dns server ipv6 source-ip fc00:1::1

```

# Set the source IPv6 address of the local device in vpn1 to fc00:1::2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] dns server ipv6 source-ip vpn-instance vpn1 fc00:1::2

```