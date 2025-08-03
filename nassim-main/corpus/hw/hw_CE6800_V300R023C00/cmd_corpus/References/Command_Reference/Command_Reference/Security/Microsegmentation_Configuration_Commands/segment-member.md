segment-member
==============

segment-member

Function
--------



The **segment-member ip** command adds a specified IPv4 address to an EPG.

The **undo segment-member ip** command deletes a specified IPv4 address from an EPG.

The **segment-member ipv6** command adds a specified IPv6 address to an EPG.

The **undo segment-member ipv6** command deletes a specified IPv6 address from an EPG.



By default, no member is added to an EPG.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**segment-member ip** *ip-address* { *ip-address-netmask* | *mask-length* } [ **vpn-instance** *vpn-instance-name* ]

**segment-member ipv6** *ipv6-addr* { *ipv6-masklen* | *ipv6-netmask* } [ **vpn-instance** *vpn-instance-name* ]

**undo segment-member ip** *ip-address* { *ip-address-netmask* | *mask-length* } [ **vpn-instance** *vpn-instance-name* ]

**undo segment-member ipv6** *ipv6-addr* { *ipv6-masklen* | *ipv6-netmask* } [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address-netmask* | Specifies the mask length of an IPv4 address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of an IPv4 address. | The value is an integer ranging from 1 to 32. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. \_public\_ cannot be used as the VPN instance name. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |
| **ipv6** *ipv6-addr* | Specifies the IPv6 destination address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *ipv6-masklen* | Specifies the length of the IPv6 address mask. | The value is an integer ranging from 1 to 128. |
| *ipv6-netmask* | Specifies the IPv6 address mask. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **ip** *ip-address* | Specifies an IPv4 address. | The value is in dotted decimal notation. |



Views
-----

Traffic segment view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a data center network, servers can be added to EPGs based on certain rules, and GBPs can be deployed based on EPGs to implement traffic control between servers. You can run the **segment-member** command to add a specified server to an EPG.

**Precautions**

* The value range of ip-address in this command is as follows:
* Class A, class B, and class C addresses, except the 127 network segment addresses, can be used as configuration addresses.
* Class D addresses are multicast addresses and cannot be used as configuration addresses.
* Class E addresses are reserved and cannot be used as configuration addresses.
* In this command, the value range of ipv6-addr is as follows:
* Multicast address FF00::/8, which cannot be used as a configuration address.
* Loopback address::1/128, which cannot be used as a configuration address.
* Link-local address FE80::/10, which cannot be used as a configuration address.
* Embedded address::ffff:x.x.x.x/96. If x.x.x.x is not within the configurable ip-address range, the embedded address cannot be used as the configured address.
* Except the preceding addresses, all addresses can be used as configuration addresses.

Example
-------

# Add the server on network segment 192.168.32.0/24 to EPG 32768.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment segment-id 32768
[*HUAWEI-traffic-segment-32768] segment-member ip 192.168.32.0 24

```

# Add the server on network segment 2001:db8:1::1/64 to EPG 32768.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable
[*HUAWEI] traffic-segment segment-id 32768
[*HUAWEI-traffic-segment-32768] segment-member ipv6 2001:db8:1::1 64

```