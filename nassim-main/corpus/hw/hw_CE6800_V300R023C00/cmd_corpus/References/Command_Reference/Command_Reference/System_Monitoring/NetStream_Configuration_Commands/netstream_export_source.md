netstream export source
=======================

netstream export source

Function
--------



The **netstream export source** command configures the source IP address for the exported packets carrying flow statistics.

The **undo netstream export source** command deletes the configured source IP address for the exported packets carrying flow statistics.



By default, the source IP address of the exported packets carrying flow statistics is not configured.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **source** { *ip-address* | **ipv6** *ipv6-address* }

**undo netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **source** [ *ip-address* | **ipv6** [ *ipv6-address* ] ]

For CE6885-LL (low latency mode):

**netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **source** *ip-address*

**undo netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **source** [ *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the source IPv4 address of the exported packets carrying flow statistics. | The value is in dotted decimal notation. |
| **ip** | Specifies source IP address for the exported packets carrying IPv4 flow statistics. | - |
| **ipv6** | Specifies the source IP address for the exported packets carrying IPv6 flow statistics. | - |
| **ipv6** *ipv6-address* | Specifies the source IPv6 address of the exported packets carrying flow statistics.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |
| **vxlan** | Specifies the source IP address for the exported packets carrying VXLAN flexible flow statistics. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If the NMS needs to identify the data source according to the source IP address in NetStream packets, specify the source IP address for NetStream packets.

**Precautions**

* If the source IP address of exported packets is not specified, packets are not exported. The source address of the exported packets carrying IPv4 flow statistics, IPv6 flow statistics, or VXLAN flexible flow statistics can be an IPv4 or IPv6 address. The source IP address and the destination IP address (NSC address) of exported packets must be routable to each other. Two source addresses (an IPv4 address and an IPv6 address) can be configured for different exported packets carrying flow statistics. The two addresses are independent of each other.For the CE6885-LL working in low latency mode, only the source IPv4 address can be used for exporting packets, and only one source IPv4 address can be configured for exporting packets carrying different flow statistics.
* The IP addresses of the local and peer devices bound to a VPN instance must be different. In addition, the addresses cannot be set to unspecified addresses, IPv6 link-local addresses, multicast addresses, or loopback addresses.


Example
-------

# In the system view, set the source address for the exported packets carrying IPv4 flow statistics to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] netstream export ip source 10.1.1.1

```