peer public-as-only import (BGP-VPN-Target address family view)
===============================================================

peer public-as-only import (BGP-VPN-Target address family view)

Function
--------



The **peer public-as-only import** command enables a device to remove private AS numbers from the AS\_Path list in received BGP Update messages.

The **undo peer public-as-only import** command allows a device to accept BGP Update messages in which the AS\_Path list carries private AS numbers.



By default, a device does not remove private AS numbers from the AS\_Path list when receiving BGP Update messages.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **public-as-only** **import** [ **force** ]

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **public-as-only** **import** **disable**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **public-as-only** **import** [ **force** ]

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **public-as-only** **import** **disable**

For CE6885-LL (low latency mode):

**peer** *peerIpv4Addr* **public-as-only** **import** [ **force** ]

**peer** *peerIpv4Addr* **public-as-only** **import** **disable**

**undo peer** *peerIpv4Addr* **public-as-only** **import** [ **force** ]

**undo peer** *peerIpv4Addr* **public-as-only** **import** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **force** | Deletes all private AS numbers from the AS\_Path attribute. | - |
| **disable** | Disables a device from removing the private AS numbers from the AS\_Path list in received BGP Update messages. | - |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Generally, AS numbers range from 1 to 4294967295, including the public, private, and reserved AS numbers. If the **private-4-byte-as enable** command is not run, private AS numbers range from 64512 to 65534, and the AS number 65535 is reserved for special use. If the **private-4-byte-as enable** command is run, private AS numbers range from 64512 to 65534 and from 4200000000 to 4294967294, and the AS numbers 65535 and 4294967295 are reserved for special use.Public AS numbers can be used over the Internet, whereas private AS numbers cannot be advertised to the Internet. If private AS numbers are advertised to the Internet, routing loops may occur. Therefore, private AS numbers are used only within a routing domain.This command enables BGP to process the private and reserved AS numbers in the AS\_Path attribute of BGP routes as required. Reserved AS numbers are processed the same as private AS numbers. The following uses private AS numbers as an example to illustrate the processing modes:If the **peer public-as-only import** command is run without any optional parameter specified and the AS\_Path attribute of BGP routes contains only private AS numbers, BGP deletes these private AS numbers and then accepts update messages. If the AS\_Path contains both public and private AS numbers, BGP does not delete the private AS numbers. If private AS numbers are deleted in this case, a forwarding error may occur. To forcibly delete private AS numbers from the AS\_Path, configure force.


Example
-------

# Enable a BGP device to remove all the private AS numbers from the AS\_Path list in BGP Update messages received from a specified peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.2.2.2 as-number 200
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 public-as-only import

```