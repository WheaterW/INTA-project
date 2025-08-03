ipv6 pathmtu
============

ipv6 pathmtu

Function
--------



The **ipv6 pathmtu** command sets a static path maximum transmission unit (PMTU) for a specified destination IPv6 address.

The **undo ipv6 pathmtu** command deletes the static PMTU set for a specified destination IPv6 address.



By default, no static PMTU is set for a specified destination IPv6 address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 pathmtu** *ipv6-address* [ **vpn-instance** *vpn-instance-name* ] [ *path-mtu* ]

**undo ipv6 pathmtu** *ipv6-address* [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address for which a PMTU is to be set. | The address is a 32-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X. The address can be a unicast address only. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of an IPv6 VPN instance for which a PMTU is to be set. | The value is a string of 1 to 31. |
| *path-mtu* | Specifies the path MTU, that is, the maximum size of IPv6 packets allowed to be sent along the path. | The value is an integer ranging from 1280 to 10000, in bytes. The default value is 1500. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A Path Maximum Transmission Unit (PMTU) is used to determine the proper size of packets to be transmitted along the path from a source to a destination. Commonly, a device fragments and forwards packets based on the dynamic PMTU learning function of the system, trying not to fragment packets during transmission. In this manner, loads on intermediate Routers are reduced and effective network resource use.In some special cases, however, to protect devices on the network and avoid the large-sized packet attacks, you can run the **ipv6 pathmtu** command to set a static PMTU for the specified destination IPv6 address to control the maximum size of packets that can be transmitted between the source and the destination.

**Configuration Impact**

On the path along which packets are transmitted, a node discards the received packets if its MTU is smaller than the PMTU of the received packets. Therefore, in most cases, dynamic PMTU learning is recommended unless there are security vulnerabilities on the network. You do not need to run the **ipv6 pathmtu** command to set a static PMTU, that is, use the default PMTU.

**Precautions**

The priorities of the static PMTU, dynamic PMTU, and default PMTU of the system are in a descending order.


Example
-------

# Set the PMTU for the address 2001:db8::1 in the IPv6 VPN instance to 1600 bytes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn6
[*HUAWEI-vpn-instance-vpn6] ipv6-family
[*HUAWEI-vpn-instance-vpn6-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn6] quit
[*HUAWEI] ipv6 pathmtu 2001:db8::1 vpn-instance vpn6 1600

```

# Set the PMTU for the specified IPv6 address to 1300 bytes.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 pathmtu 2001:db8::12 1300

```