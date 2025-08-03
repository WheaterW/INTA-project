dns server ipv6
===============

dns server ipv6

Function
--------



The **dns server ipv6** command specifies a DNS server IPv6 address.

The **undo dns server ipv6** command deletes a DNS server IPv6 address.



By default, no DNS server IPv6 address is specified.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dns server ipv6** *ipv6-address* [ { *interface-type* *interface-number* | *interface-name* } ] [ **vpn-instance** *vpn-instance-name* ]

**undo dns server ipv6** [ *ipv6-address* [ { *interface-type* *interface-number* | *interface-name* } ] [ **vpn-instance** *vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address for a DNS server. | The value is a 128-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X, with each X representing four hexadecimal numbers. |
| *interface-type* | Specifies the type of an outbound interface that communicates with the DNS server. | - |
| *interface-number* | Specifies the number of an outbound interface that communicates with the DNS server. | - |
| *interface-name* | Specifies the name of the outbound interface communicating with the DNS server. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The DNS client must work with the DNS server to implement dynamic domain name resolution. You can run the **dns server ipv6** command to specify the IPv6 address of the DNS server. The DNS client sends requests to the specified DNS server for domain name resolution.During dynamic domain name resolution, the switch sends a domain name resolution request to the DNS servers according to the order in which they were configured. If the domain name resolution request on the first DNS server times out, the device sends the request to the next DNS server.

**Precautions**

* The IPv6 address of the DNS server must be a global unicast address or link-local address.
* If the IPv6 address of the DNS server is configured as a link-local address, you must specify the outbound interface (excluding the loopback interface) for communicating with the DNS server.
* If the IPv6 address of the DNS server is configured as a global unicast address, you cannot specify the outbound interface for communicating with the DNS server.
* The new configuration overwrites the original configuration only when the IPv6 addresses and VPN instances are the same.
* A maximum of six DNS server IP addresses can be configured on the device.

Example
-------

# Set the IPv6 address of the DNS server in vpn1 to 2001:db8::2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] dns server ipv6 2001:db8::2 vpn-instance vpn1

```

# Set the IPv6 address of the DNS server to 2001:db8::1.
```
<HUAWEI> system-view
[~HUAWEI] dns server ipv6 2001:db8::1

```